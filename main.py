#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function # Only Python 2.x
from Tkinter import *
import time;
import subprocess
import matplotlib
import threading
import ttk
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import os
import signal
import MySQLdb
import string
import random

# Textbox values to be currently diplayed by ARB ID managemant
boxcounter = 0
global stats
stats = {}

# Selected CANinterface to connect to
global CANinterface
global interface_stored
global stop
interface_stored = 0
CANinterface = ""
stop = False


def execute(cmd):
    global popen
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        return

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("can-utils X")

        # Prepare grid
        for r in range(7):
            self.master.rowconfigure(r, weight=1)
        for c in range(5):
            self.master.columnconfigure(c, weight=1)

        # System Initializations
        interface_stored = 0

        # Buttons
        #button1 = Button(master, text="Configure Graph 1", command=self.create_window_Graph1).grid(row=7,column=0,sticky=E+W)
        button2 = Button(master, text="Vehicle Select", command=self.create_window_VehSel).grid(row=7,column=1,sticky=E+W) #Injection Rules
        button3 = Button(master, text="Play Simulation", command=self.playcaps).grid(row=7,column=2,sticky=E+W)
        button4 = Button(master, text="Fuzzing", command=self.create_window_StartFuzz).grid(row=7,column=3,sticky=E+W)
        button5 = Button(master, text="Live Monitoring", command= lambda: self.create_window_LiveMonitoring(x1, x2, y1, y2)).grid(row=7,column=4,sticky=E+W)
        button8 = Button(master, text="Inject Packet", command=self.pkt_win).grid(row=8,column=1,sticky=E+W) #/Sequence
        button9 = Button(master, text="Capture Simulation", command=self.create_window_StartCapture).grid(row=8,column=2,sticky=E+W)
        button10 = Button(master, text="End/Save Capture", command=self.stopcap).grid(row=8,column=3,sticky=E+W)
        button11 = Button(master, text="Exit", command=self.close_window).grid(row=8,column=4,sticky=E+W)

        self.TextArea = Text(master, height=3.5, width=51)
        ScrollBar = Scrollbar(master)
        ScrollBar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=ScrollBar.set)
        ScrollBar.grid(row= 7, rowspan=2, column=0, sticky=E)
        self.TextArea.grid(row= 7, rowspan=2, column=0, sticky=W)

        # Graph 1
        canvas1 =Canvas(master, borderwidth=0)
        Frame1 = Frame(canvas1, bg="red")
        Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 1, sticky = W+E+N+S) 
        canvas1.grid(row = 0, column = 0, rowspan = 3, columnspan = 1, sticky = W+E+N+S)
        canvas1.create_window((1,1), window=Frame1, anchor="w")
        self.f = Figure(figsize=(3,4), dpi=100)
        self.ax1 = self.f.add_subplot(111)

        #Plotting
        x1 = []
        y1 = []

        self.canvas = FigureCanvasTkAgg(self.f, master=root)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row = 0, column = 0, rowspan = 3, columnspan = 1, sticky = W+E+N+S) 

        # Graph 2
        canvas2 = Canvas(master, borderwidth=0, background="#ffffff")
        Frame2 = Frame(canvas2, bg="red")
        Frame2.grid(row = 3, column = 0, rowspan = 3, columnspan = 1, sticky = W+E+N+S)
        canvas2.grid(row = 3, column = 0, rowspan = 3, columnspan = 1, sticky = W+E+N+S)
        canvas2.create_window((1,1), window=Frame2, anchor="w")
        self.f1 = Figure(figsize=(3,4), dpi=100)
        self.ax2 = self.f1.add_subplot(111)

        #Plotting 
        x2 = []
        y2 = []

        self.canvas4 = FigureCanvasTkAgg(self.f1, master=root)
        self.canvas4.show()
        self.canvas4.get_tk_widget().grid(row = 3, column = 0, rowspan = 3, columnspan = 1, sticky = W+E+N+S)

        # Incoming Traffic
        canvas3 = Canvas(master, borderwidth=0, background="#ffffff")
        #Textbox Frame
        global Frame3
        Frame3 = Frame(canvas3, background="#ffffff")
        Frame3.grid(row = 1, column = 2, rowspan = 6, columnspan = 6, sticky = W+E+N+S)
        Frame3.bind("<Configure>", lambda event, canvas=canvas3: self.onFrameConfigure(canvas3))
        # ADD THE TEXTBOXES
        vsb = Scrollbar(master, orient="vertical", command=canvas3.yview)
        canvas3.configure(yscrollcommand=vsb.set)
        vsb.grid(row = 0, column = 6, rowspan = 6, columnspan = 1, sticky = W+E+N+S)
        canvas3.grid(row = 0, column =1, rowspan = 6, columnspan = 6, sticky = W+E+N+S)
        canvas3.create_window((4,4), window=Frame3, anchor="w")

        # Create column headers at the top and initialize cells
        self.tree = ttk.Treeview(canvas3)
        self.tree["columns"]= ("TS(abs)","ARB ID", "DLC", "BYTE 1", "BYTE 2", "BYTE 3", "BYTE 4", "BYTE 5", "BYTE 6", "BYTE 7", "BYTE 8")
        self.tree["show"] = "headings" # remove first empty column (id)

        # Initialize sizes of cells
        self.tree["height"] = 5000
        for x in self.tree["columns"]:
            self.tree.column(x, width=70)
            self.tree.heading(x, text=x)

        # Add clear cells to begin with
        for i in range(0,100):
            self.tree.insert("",i,values=("","", "", "", "", "", "", "", "", "", ""),tags = ('clean',))

        # Declare labels for FILTERS, NEWEST MESSAGE, BYTE UPDATES
        self.tree.tag_configure('clean', background='orange')
        self.tree.tag_configure('occupied', background='yellow')
        self.tree.tag_configure('new', background='green')
        self.tree.tag_configure('filter', background='red')
        self.tree.grid_rowconfigure(0, weight = 1)
        self.tree.grid_columnconfigure(0, weight = 1)
        self.tree.grid(sticky = (N,S,W,E))
        self.tree.pack()

        self.VEHICLE_NAME = ""

        # Welcome the user
        self.TextArea.insert(END, "Welcome!\nPlease select an option to the right to begin.\n")

        # For graph
        self.x = []
        self.y = []
        self.TRAFFIC = {}
        self.mode = 0 # 0 = No graph, 1 = Frequency, 2 = Integral

    def plot1(self, x, y, ticks, strlab, ID):
        self.f = Figure(figsize=(3,4), dpi=100)
        self.ax1 = self.f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.f, master=root)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row = 0, column = 0, rowspan = 3, columnspan = 1, sticky = W+E+N+S) 
        self.ax1.set_xticklabels(ticks)

        for tick in self.ax1.xaxis.get_major_ticks():
            tick.label.set_fontsize(6)
            # specify integer or one of preset strings, e.g.
            #tick.label.set_fontsize('x-small') 
            tick.label.set_rotation(30)

        if(strlab == "INT"):
            self.ax1.set_title('Integral Graph: %s' % ID)
        if(strlab == "FRQ"):
            self.ax1.set_title('Frequency Graph: %s' % ID)

        self.ax1.plot(x,y)


    def plot2(self, x, y, ticks, strlab, ID):
        self.f1 = Figure(figsize=(3,4), dpi=100)
        self.ax2 = self.f1.add_subplot(111)
        self.canvas4 = FigureCanvasTkAgg(self.f1, master=root)
        self.canvas4.show()
        self.canvas4.get_tk_widget().grid(row = 3, column = 0, rowspan = 3, columnspan = 1, sticky = W+E+N+S)
        self.ax2.set_xticklabels(ticks)

        for tick in self.ax2.xaxis.get_major_ticks():
            tick.label.set_fontsize(6)
            # specify integer or one of preset strings, e.g.
            #tick.label.set_fontsize('x-small') 
            tick.label.set_rotation(30)

        if(strlab == "INT"):
            self.ax2.set_title('Integral Graph: %s' % ID)
        if(strlab == "FRQ"):
            self.ax2.set_title('Frequency Graph: %s' % ID)

        self.ax2.plot(x,y)

    # Search tree by ARB ID
    def search(self, desired):
        for child in self.tree.get_children():

            # Isolate part of child to compare with (ARB ID)
            text = self.tree.item(child)
            text = str(text['values'][1])

            if text.startswith(desired):
                # Focus on the found object in the treeview
                self.tree.selection_set(child)

                # Return True and child object if found
                return [True, child]

        return [False, 0]

    def addCar(self, Vtree, model, make, trim):
        if(model == "" or make == "" or trim == ""):
            self.TextArea.insert(END, "Please enter the model, make, and trim of the vehicle to register.\n")
            return

        checkCar= False
        newCar = "%s_%s_%s" % (model, make, trim)

        db = MySQLdb.connect("localhost","root","toor")
        cursor = db.cursor()

        sql = "SHOW DATABASES;"
        try:
            # Execute the SQL command
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                if(row[0] == newCar):
                    checkCar = True
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        if(checkCar == False):
            sql = "CREATE DATABASE %s;" % (newCar)
            try:
                # Execute the SQL command
                cursor.execute(sql)
                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

            sql = "SHOW DATABASES;"
            count = 0
            try:
                # Execute the SQL command
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    if(row != "performance_schema" and row!= "information_schema" and row!= "mysql"):
                        Vtree.insert("",count,values=(row), tags = ('vehicle',))
                        count = count + 1

                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

            db.close()

    def regCar(self, DBname):
        if(DBname == ""):
            self.TextArea.insert(END, "Please select a vehicle to register.\n")
            return
        else:
            self.VEHICLE_NAME = DBname
            self.TextArea.insert(END, "%s vehicle selected!.\n" % self.VEHICLE_NAME)
            return

    # For window managemant
    def create_window_VehSel(self):
        x = Toplevel(root)
        x.geometry("410x350+200+200")
        x.wm_title("Vehicle Selection")

        Label(x, text="Vehicle Model:", width=25, relief=RAISED).grid(row=0, column=0, columnspan=3, sticky=N+S+E+W)
        Label(x, text="Vehicle Make:", width=25, relief=RAISED).grid(row=1, column=0, columnspan=3, sticky=N+S+E+W)
        Label(x, text="Vehicle Trim:", width=25, relief=RAISED).grid(row=2, column=0, columnspan=3, sticky=N+S+E+W)

        model = Entry(x)
        model.grid(row=0, column=3, columnspan=3, sticky=N+S+E+W)
        model.focus_set()

        make= Entry(x)
        make.grid(row=1, column=3, rowspan=1, columnspan=3, sticky=N+S+E+W)

        trim= Entry(x)
        trim.grid(row=2, column=3, rowspan=1, columnspan=3, sticky=N+S+E+W)

        # Create area for vehicle table
        canvas = Canvas(x, borderwidth=0, background="#ffffff")
        #Textbox Frame
        frame = Frame(canvas, background="#ffffff")
        canvas.create_window((4,4), window=frame, anchor="w")

        canvas.grid(row = 4, column =0, rowspan = 3, columnspan = 6, sticky = N+S)
        frame.grid(row = 4, column =0, rowspan = 3, columnspan = 6, sticky = N+S)

        # Create column headers at the top and initialize cells
        Vtree = ttk.Treeview(canvas)
        Vtree["columns"]= ("Registered Vehicles",)
        Vtree["show"] = "headings" # remove first empty column (id)

        # Initialize sizes of cells
        Vtree["height"] = 10
        for V in Vtree["columns"]:
            Vtree.column(V, width=400)
            Vtree.heading(V, text=V)

        Vtree.tag_configure('vehicle', background='green')
        Vtree.grid_rowconfigure(0, weight = 1)
        Vtree.grid_columnconfigure(0, weight = 1)
        Vtree.grid(sticky = (N,S))


        db = MySQLdb.connect("localhost","root","toor")
        cursor = db.cursor()
        sql = "SHOW DATABASES;"
        count = 0
        try:
            # Execute the SQL command
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                if(row[0] != "performance_schema" and row[0]!= "information_schema" and row[0]!= "mysql"):
                    Vtree.insert("",count,values=(row), tags = ('vehicle',))
                    count = count + 1

            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()


        b = Button(x,text='Log In', command=lambda: self.regCar(Vtree.item(Vtree.selection()[0],"values")[0]))
        b.grid(row=7, column=0, columnspan=6, stick=N+S+E+W)

        addCars = Button(x,text='Add Vehicle', height=1, command=lambda: self.addCar(Vtree, model.get(), make.get(), trim.get()))
        addCars.grid(row=3, column=0, rowspan=1, columnspan=6, sticky=N+S+E+W)

    def startCap(self):
        stop = False
        thread = threading.Thread(target=self.Cap, args=())
        thread.daemon = True
        thread.start()

    def stopcap(self):
        stop = True
        self.TextArea.insert(END, "Packet dump ended, connection to CAN interface closed.\n")

    def Cap(self):
        # Name of simulation
        tablename = c.get()
        countstr = d.get()
        numExists = False

        if countstr!= "":
            num = int(countstr)
            numExists = True


        # Connect to database and create a table for the simulation
        # Open database connection
        db = MySQLdb.connect("localhost","root","toor",self.VEHICLE_NAME )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        try:
            # Drop table if it already exist using execute() method
            cursor.execute("DROP TABLE IF EXISTS %s" % tablename)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        # Create table
        sql = "CREATE TABLE %s (TS INT, ARB_ID CHAR(8), DLC CHAR(8), B1 CHAR(8), B2 CHAR(8), B3 CHAR(8), B4 CHAR(8), B5 CHAR(8), B6 CHAR(8), B7 CHAR(8), B8 CHAR(8) )" % tablename

        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        # Now prepare to insert traffic
        global rows
        rows = 0
        count = 0

        # Connect to interface:
        cmd = "exec candump %s -t a" % b.get()
        for line in execute([cmd]):
            words = line.split()

            # SEARCH TABLE FOR CURRENT ARB ID
            [exists, dupid] = self.search(words[2])

            if(count !=0):
                self.tree.item(lastid, tags=('clean',))

            # IF ARB ID DOES NOT EXIST IN TABLE, CREATE
            if exists != True:
                # Get the current time
                currtime = words[0][words[0].index("(") + 1:words[0].rindex(".")]
                timestr = time.strftime('%H:%M:%S',  time.gmtime(int(currtime)))

                # Insert into UI
                itemid = self.tree.insert("",rows,values=(timestr,words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10],words[11]),tags = ('new',))
                lastid= itemid
                rows = rows+1

            # IF ALREADY EXISTS, UPDATE
            else:
                # Get the current time
                currtime = words[0][words[0].index("(") + 1:words[0].rindex(".")]
                timestr = time.strftime('%H:%M:%S',  time.gmtime(int(currtime)))

                # Insert into UI
                self.tree.item(dupid, text="", values=(timestr,words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10],words[11]),tags = ('new',))
                lastid = dupid

            count = count + 1

            # Get timestamp as an int for database
            currtime = int(words[0][words[0].index("(") + 1:words[0].rindex(".")])
            # Now insert into the database
            sql = "INSERT INTO %s (TS, ARB_ID, DLC, B1, B2, B3, B4, B5, B6, B7, B8 ) VALUES ('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' ,'%s', '%s');" % (tablename,currtime,words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10],words[11])

            # Execute insertion
            try:
                # Execute the SQL command
                cursor.execute(sql)
                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

            # If the stop button is pressed
            if stop == True:
                # Disconnect from server
                db.close()
                popen.kill()

            # Stop at desired packet capture count if enabled
            if numExists == True:
                if count >= num:
                    # Disconnect from server
                    db.close()
                    popen.kill()

# For playing traffic back to the CAN bus
    def playback(self, table):
        if(self.VEHICLE_NAME == ""):
                self.TextArea.insert(END, "Please register/log in to a vehicle.\n")
                return

        # Open database connection
        db = MySQLdb.connect("localhost","root","toor",self.VEHICLE_NAME )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        sql = "SELECT * FROM %s ;" % table
        count = 0

        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Update the Treeview
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            for row in results:
                cmd = "cansend %s %s#%s.%s%s.%s%s%s%s.%s" % (q.get(), row[1], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                for line in execute([cmd]):
                    count = count + 1

            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

    def playinit(self, string):
        thread = threading.Thread(target=self.playback, args=(string,))
        thread.daemon = True
        thread.start()

    def playcaps(self):
        if(self.VEHICLE_NAME == ""):
                self.TextArea.insert(END, "Please register/log in to a vehicle.\n")
                return

        #Create a Treeview and place all the simulation names in it
        # Incoming Traffic

        rowcount = 0
        global z
        z = Toplevel(root)
        z.geometry("425x500+200+200")
        canvas = Canvas(z, borderwidth=0, background="#ffffff")

        #Textbox Frame
        global frame
        frame = Frame(canvas, background="#ffffff")
        canvas.pack()
        canvas.create_window((4,4), window=frame, anchor="w")

        # Create column headers at the top and initialize cells
        Stree = ttk.Treeview(canvas)
        Stree["columns"]= ("SIMULATION NAME", "PACKET COUNT")
        Stree["show"] = "headings" # remove first empty column (id)

        # Initialize sizes of cells
        Stree["height"] = 20
        for x in Stree["columns"]:
            Stree.column(x, width=200)
            Stree.heading(x, text=x)

        # Declare labels for FILTERS, NEWEST MESSAGE, BYTE UPDATES
        Stree.tag_configure('clean', background='yellow')
        # self.tree.tag_configure('filter2', background='pink')
        # self.tree.tag_configure('filter3', background='pink')
        Stree.grid_rowconfigure(0, weight = 1)
        Stree.grid_columnconfigure(0, weight = 1)
        Stree.grid(sticky = (N,S,W,E))
        Stree.pack()

        # An entry item for entering the virtual CAN interface name
        global q
        qlabel = Label(z, text="Interface Name:", width=15, relief="solid")
        qlabel.pack()
        q = Entry(z)
        q.pack()
        q.focus_set()


        e = Button(z,text='Play Simulation',command= lambda: self.playinit(Stree.item(Stree.selection()[0],"values")[0]))
        e.pack(side='bottom')

        # Connect to database and create a table for the simulation
        # Open database connection
        db = MySQLdb.connect("localhost","root","toor",self.VEHICLE_NAME )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        sql = "SHOW TABLES ;"

        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Update the Treeview
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            for row in results:
                name = row[0]
                sql = "SELECT COUNT(TS) FROM %s;" % row[0]
                cursor.execute(sql)
                counts = cursor.fetchall()
                num = counts[0][0]
                Stree.insert("",rowcount,values=(name, num),tags = ('clean',))

            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()


    def create_window_StartCapture(self):

        if(self.VEHICLE_NAME == ""):
                self.TextArea.insert(END, "Please register/log in to a vehicle.\n")
                return

        global t
        t = Toplevel(root)
        t.geometry("300x150+200+200")
        t.wm_title("Start Traffic Capture")

        global b
        global c
        global d

        # An entry item for entering the virtual CAN interface name
        blabel = Label(t, text="Interface Name:", width=15, relief=RAISED)
        blabel.pack()
        b = Entry(t)
        b.pack()
        b.focus_set()

        # An entry item for entering the simulation name
        clabel = Label(t, text="Simulation Name:", width=15, relief=RAISED)
        clabel.pack()
        c = Entry(t)
        c.pack()
        c.focus_set()

        # An entry item for entering the number of packets desired, optional
        dlabel = Label(t, text="Number of Packets to Capture (optional):", width=35, relief=RAISED)
        dlabel.pack()
        d = Entry(t)
        d.pack()
        d.focus_set()

        e = Button(t,text='Begin Capture',command=self.startCap)
        e.pack(side='bottom')

    def create_window_StartFuzz(self):
        if(self.VEHICLE_NAME == ""):
                self.TextArea.insert(END, "Please register/log in to a vehicle.\n")
                return


        global po
        po = Toplevel(root)
        po.geometry("350x325+200+200")
        po.wm_title("CAN Bus Fuzzer")


        global ARB_FUZZ_NAME
        ARB_FUZZ_NAME = Entry(po)
        ARB_FUZZ_NAME.grid(row=1, column=1)
        ARB_FUZZ_NAME.focus_set()

        RAND_ARB_en = IntVar()
        CUST_ARB_en = IntVar()
        RAND_PKT_en = IntVar()
        CUST_PKT_en = IntVar()

        RANDARB = Checkbutton(po, text="Fuzz Random ARB ID's", variable=RAND_ARB_en, onvalue=1, offvalue=0)#command= lambda: self.eng)
        RANDARB.grid(row=0, column=0, sticky=N+S+E+W)
        CUSTARB = Checkbutton(po, text="Fuzz Custom ARB ID:", variable=CUST_ARB_en, onvalue=1, offvalue=0)
        CUSTARB.grid(row=1, column=0, sticky=N+S+E+W)

        RANDPKT = Checkbutton(po, text="Random Packet Injection", variable=RAND_PKT_en, onvalue=1, offvalue=0)#command= lambda: self.eng)
        RANDPKT.grid(row=2, column=0,sticky=N+S+E+W)
        CUSTPKT = Checkbutton(po, text="Custom Packet:", variable=CUST_PKT_en, onvalue=1, offvalue=0)
        CUSTPKT.grid(row=3, column=0, sticky=N+S+E+W)


        Label(po, text="B1:", relief=RAISED).grid(row=4, column=0, sticky=N+S+E+W)
        Label(po, text="B2:", relief=RAISED).grid(row=5, column=0, sticky=N+S+E+W)
        Label(po, text="B3:", relief=RAISED).grid(row=6, column=0, sticky=N+S+E+W)
        Label(po, text="B4:", relief=RAISED).grid(row=7, column=0, sticky=N+S+E+W)
        Label(po, text="B5:", relief=RAISED).grid(row=8, column=0, sticky=N+S+E+W)
        Label(po, text="B6:", relief=RAISED).grid(row=9, column=0, sticky=N+S+E+W)
        Label(po, text="B7:", relief=RAISED).grid(row=10, column=0, sticky=N+S+E+W)
        Label(po, text="B8:", relief=RAISED).grid(row=11, column=0, sticky=N+S+E+W)

        B1 = Entry(po)
        B1.grid(row=4, column=1, sticky=N+S+E+W)
        B1.focus_set()

        B2 = Entry(po)
        B2.grid(row=5, column=1, sticky=N+S+E+W)
        B2.focus_set()

        B3 = Entry(po)
        B3.grid(row=6, column=1, sticky=N+S+E+W)
        B3.focus_set()

        B4 = Entry(po)
        B4.grid(row=7, column=1, sticky=N+S+E+W)
        B4.focus_set()

        B5 = Entry(po)
        B5.grid(row=8, column=1, sticky=N+S+E+W)
        B5.focus_set()

        B6 = Entry(po)
        B6.grid(row=9, column=1, sticky=N+S+E+W)
        B6.focus_set()

        B7 = Entry(po)
        B7.grid(row=10, column=1, sticky=N+S+E+W)
        B7.focus_set()

        B8 = Entry(po)
        B8.grid(row=11, column=1, sticky=N+S+E+W)
        B8.focus_set()

        Label(po, text="CAN Interface Name:", relief=RAISED).grid(row=12, column=0, sticky=N+S+E+W)
        iname = Entry(po)
        iname.grid(row=12, column=1, sticky=N+S+E+W)
        iname.focus_set()

        Label(po, text="Packet Count:", relief=RAISED).grid(row=13, column=0, sticky=N+S+E+W)
        num = Entry(po)
        num.grid(row=13, column=1, sticky=N+S+E+W)
        num.focus_set()

        start = Button(po,text='Start',command= lambda: self.launchfuzz(self, B1, B2, B3, B4, B5, B6, B7, B8,RAND_ARB_en,CUST_ARB_en ,RAND_PKT_en , ARB_FUZZ_NAME, iname, num), height=1)
        start.grid(row=14, column=0, columnspan=2, sticky=N+S+E+W)

        RAND_ARB_en.set(0)
        CUST_ARB_en.set(0)
        RAND_PKT_en.set(0)
        CUST_PKT_en.set(0)

    def pkt_win(self):

        if(self.VEHICLE_NAME == ""):
                self.TextArea.insert(END, "Please register/log in to a vehicle.\n")
                return


        pktin = Toplevel(root)
        pktin.geometry("300x260+200+200")
        pktin.wm_title("CAN Bus Packet Injection")

        Label(pktin, text="Arbitration ID:", relief=RAISED).grid(row=0, column=0, sticky=N+S+E+W)
        ARB_INJ_NAME = Entry(pktin)
        ARB_INJ_NAME.grid(row=0, column=1)
        ARB_INJ_NAME.focus_set()


        Label(pktin, text="B1:", relief=RAISED).grid(row=2, column=0, sticky=N+S+E+W)
        Label(pktin, text="B2:", relief=RAISED).grid(row=3, column=0, sticky=N+S+E+W)
        Label(pktin, text="B3:", relief=RAISED).grid(row=4, column=0, sticky=N+S+E+W)
        Label(pktin, text="B4:", relief=RAISED).grid(row=5, column=0, sticky=N+S+E+W)
        Label(pktin, text="B5:", relief=RAISED).grid(row=6, column=0, sticky=N+S+E+W)
        Label(pktin, text="B6:", relief=RAISED).grid(row=7, column=0, sticky=N+S+E+W)
        Label(pktin, text="B7:", relief=RAISED).grid(row=8, column=0, sticky=N+S+E+W)
        Label(pktin, text="B8:", relief=RAISED).grid(row=9, column=0, sticky=N+S+E+W)

        B1 = Entry(pktin)
        B1.grid(row=2, column=1, sticky=N+S+E+W)
        B1.focus_set()

        B2 = Entry(pktin)
        B2.grid(row=3, column=1, sticky=N+S+E+W)
        B2.focus_set()

        B3 = Entry(pktin)
        B3.grid(row=4, column=1, sticky=N+S+E+W)
        B3.focus_set()

        B4 = Entry(pktin)
        B4.grid(row=5, column=1, sticky=N+S+E+W)
        B4.focus_set()

        B5 = Entry(pktin)
        B5.grid(row=6, column=1, sticky=N+S+E+W)
        B5.focus_set()

        B6 = Entry(pktin)
        B6.grid(row=7, column=1, sticky=N+S+E+W)
        B6.focus_set()

        B7 = Entry(pktin)
        B7.grid(row=8, column=1, sticky=N+S+E+W)
        B7.focus_set()

        B8 = Entry(pktin)
        B8.grid(row=9, column=1, sticky=N+S+E+W)
        B8.focus_set()

        Label(pktin, text="CAN Interface Name:", relief=RAISED).grid(row=10, column=0, sticky=N+S+E+W)
        iname = Entry(pktin)
        iname.grid(row=10, column=1, sticky=N+S+E+W)
        iname.focus_set()

        Label(pktin, text="Packet Count:", relief=RAISED).grid(row=11, column=0, sticky=N+S+E+W)
        num = Entry(pktin)
        num.grid(row=11, column=1, sticky=N+S+E+W)
        num.focus_set()

        start = Button(pktin,text='Start',command= lambda: self.launchinj(B1, B2, B3, B4, B5, B6, B7, B8, ARB_INJ_NAME, iname, num), height=1)
        start.grid(row=12, column=0, columnspan=2, sticky=N+S+E+W)

    def launchinj(self, B1, B2, B3, B4, B5, B6, B7, B8, ARB_INJ_NAME, iname, num):
        thread = threading.Thread(target=self.startInj, args=(B1, B2, B3, B4, B5, B6, B7, B8, ARB_INJ_NAME, iname, num))
        thread.daemon = True
        thread.start()

    def startInj(self, B1, B2, B3, B4, B5, B6, B7, B8, ARB_INJ_NAME, iname, num):
        cmd = "cansend %s %s#%s.%s%s.%s%s%s%s.%s" % (iname.get(),ARB_INJ_NAME.get(), B1.get(),B2.get(),B3.get(),B4.get(),B5.get(),B6.get(),B7.get(),B8.get())
        pcount = int(num.get())

        for i in range(pcount):
            for line in execute([cmd]):
                words = line.split()

        self.TextArea.insert(END, "%d CAN packet(s) injected.\nTarget ARB ID: %s\n" % (pcount,ARB_INJ_NAME.get()))


    # Returns True if table exists in the TRAFFIC database
    def checkTrafficTable(self,table):

        found = 0

        db = MySQLdb.connect("localhost","root","toor", self.VEHICLE_NAME )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        try:
            # Check if the tags database exists
            cursor.execute("SHOW TABLES LIKE '%s';" % table)
            results = cursor.fetchall()

            for row in results:
                if(row[0] == table):
                    found = 1

            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()

        return(found)


    def startMon(self,g1enabled,g2enabled,g1fenable,g2fenable,g1tenable,g2tenable, x1, x2, y1, y2, ArbEntry1, ArbEntry2,FrqEntry1, FrqEntry2, iname, pcount):
        stop = False
        thread = threading.Thread(target=self.Mon, args=(g1enabled,g2enabled,g1fenable,g2fenable,g1tenable,g2tenable, x1, x2, y1, y2, ArbEntry1, ArbEntry2,FrqEntry1, FrqEntry2, iname, pcount))
        thread.daemon = True
        thread.start()

    def Mon(self,g1enabled,g2enabled,g1fenable,g2fenable,g1tenable,g2tenable, x1, x2, y1, y2, ArbEntry1, ArbEntry2,FrqEntry1, FrqEntry2, iname, pcount):

        count = 0
        global rows
        rows = 0
        xticks1 = []
        xticks2 = []

        # For frq graphs
        p1fcount = 0
        p2fcount = 0
        last_time1 = 0
        last_time2 = 0

        # Grab interface name, formulate command
        cmd = "exec candump %s -t a" % iname.get()

        # Check if max packet count entered
        countstr = pcount.get()
        numExists = False

        if countstr!= "":
            num = int(countstr)
            numExists = True

        # Prepare graphs if enabled
        if(g1enabled.get()):
            arbid1 = ArbEntry1.get()
            if(g1fenable.get()):
                interval1 = int(FrqEntry1.get())
            if(g1tenable.get()):
                xticks1 = []

        if(g2enabled.get()):
            arbid2 = ArbEntry2.get()
            if(g2fenable.get()):
                interval2 = int(FrqEntry2.get())
            if(g2tenable.get()):
                xticks2 = []

        # Prepare table for graphing and aggregating purposes
        # Open database connection
        db = MySQLdb.connect("localhost","root","toor",self.VEHICLE_NAME )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        try:
            # Drop table if it already exist using execute() method
            cursor.execute("DROP TABLE IF EXISTS LIVE_MON")
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        # Create table
        sql = "CREATE TABLE LIVE_MON (TS INT, ARB_ID CHAR(8), DLC CHAR(8), B1 CHAR(8), B2 CHAR(8), B3 CHAR(8), B4 CHAR(8), B5 CHAR(8), B6 CHAR(8), B7 CHAR(8), B8 CHAR(8) )"

        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        # Enable tags if they exist
        taglist = []
        tagsexists = self.checkTrafficTable("tags")

        if(tagsexists):
            # Connect to database and check for tags
            # Open database connection
            db = MySQLdb.connect("localhost","root","toor",self.VEHICLE_NAME)
            # prepare a cursor object using cursor() method
            cursor = db.cursor()
            try:
                # Check if the tags database exists
                cursor.execute("SELECT * FROM tags;")
                results = cursor.fetchall()

                for row in results:
                    taglist.append(row[0])

                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

        # Clear the table first
        x = self.tree.get_children()
        for item in x: self.tree.delete(item)

        # Add clear cells to begin with
        for i in range(0,100):
            self.tree.insert("",i,values=("","", "", "", "", "", "", "", "", "", ""),tags = ('clean',))

        current_ms_time = lambda: int(round(time.time() * 1000))

        # Connect to interface:
        for line in execute([cmd]):
            words = line.split()

            # SEARCH TABLE FOR CURRENT ARB ID
            [exists, dupid] = self.search(words[2])

            if(count !=0):
                self.tree.item(lastid, tags=('clean',))

            if(count == 0):
                p1fcount = 0
                p2fcount = 0
                last_time1 = current_ms_time()
                last_time2 = current_ms_time()
                frqcount1 = 0
                frqcount2 = 0

            # IF ARB ID DOES NOT EXIST IN TABLE, CREATE
            if exists != True:
                # Get the current time
                currtime = words[0][words[0].index("(") + 1:words[0].rindex(".")]
                timestr = time.strftime('%H:%M:%S',  time.gmtime(int(currtime)))

                # Insert into UI, enable tags
                if(words[2] in taglist):
                    itemid = self.tree.insert("",rows,values=(timestr,words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10],words[11]),tags = ('filter',))
                    self.TextArea.insert(END, "Detected CAN packet from ARB ID = %s\n" % words[2])
                else:
                    itemid = self.tree.insert("",rows,values=(timestr,words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10],words[11]),tags = ('new',))

                lastid= itemid
                rows = rows+1

            # IF ALREADY EXISTS, UPDATE
            else:
                # Get the current time
                currtime = words[0][words[0].index("(") + 1:words[0].rindex(".")]
                timestr = time.strftime('%H:%M:%S',  time.gmtime(int(currtime)))

                # Insert into UI, enable tags
                if(words[2] in taglist):
                    self.tree.item(dupid, text="", values=(timestr,words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10],words[11]),tags = ('filter',))
                    self.TextArea.insert(END, "Detected CAN packet from ARB ID = %s\n" % words[2])
                else:
                    self.tree.item(dupid, text="", values=(timestr,words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10],words[11]),tags = ('new',))
                lastid = dupid

            # Insert into temporary table:
            # Get timestamp as an int for database
            currtime = int(words[0][words[0].index("(") + 1:words[0].rindex(".")])
            # Now insert into the database
            sql = "INSERT INTO LIVE_MON (TS, ARB_ID, DLC, B1, B2, B3, B4, B5, B6, B7, B8 ) VALUES ('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' ,'%s', '%s');" % (currtime,words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10],words[11])

            # Execute insertion
            try:
                # Execute the SQL command
                cursor.execute(sql)
                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

            # For the graph
            currtime = words[0][words[0].index("(") + 1:words[0].rindex(".")]
            timestr = time.strftime('%H:%M:%S',  time.gmtime(int(currtime)))

            # Update graphs if enabled
            if(g1enabled.get()):
                if(words[2] == arbid1):
                    if(g1tenable.get()):
                        # Integral graph (1)
                        sql = "SELECT ARB_ID, count(*) as ARB_ID FROM LIVE_MON GROUP BY ARB_ID"
                        # Execute insertion
                        try:
                            # Execute the SQL command
                            cursor.execute(sql)
                            results = cursor.fetchall()

                            for row in results:
                                if(row[0] == arbid1):
                                    xticks1.append(timestr)
                                    x1.append(count)
                                    y1.append(int(row[1]))

                            # Commit your changes in the database
                            db.commit()
                        except:
                            # Rollback in case there is any error
                            db.rollback()

                        # Now plot
                        self.plot1(x1, y1, xticks1, "INT", arbid1)

                # Frequency graph        
                if(g1fenable.get()):
                    if((current_ms_time() - last_time1) >= interval1):
                        sql = "SELECT * FROM LIVE_MON ORDER BY TS DESC LIMIT %d ;" % (p1fcount+1)

                        try:
                            # Execute the SQL command
                            cursor.execute(sql)
                            results = cursor.fetchall()

                            arbcount1 = 0

                            for row in results:
                                if(row[1] == arbid1):
                                    arbcount1 = arbcount1 + 1

                            # Commit your changes in the database
                            db.commit()
                        except:
                            # Rollback in case there is any error
                            db.rollback()
                        # Now plot
                        xticks1.append(str(current_ms_time()))
                        x1.append(frqcount1)
                        y1.append(arbcount1)
                        self.plot2(x1, y1, xticks1, "FRQ", arbid1)

                        frqcount1 = frqcount1 + 1
                        p1fcount = 0
                        last_time1 = current_ms_time()


            if(g2enabled.get()):
                if(words[2] == arbid2):
                    if(g2tenable.get()):
                        # Integral graph (1)
                        sql = "SELECT ARB_ID, count(*) as ARB_ID FROM LIVE_MON GROUP BY ARB_ID"
                        # Execute insertion
                        try:
                            # Execute the SQL command
                            cursor.execute(sql)
                            results = cursor.fetchall()

                            for row in results:
                                if(row[0] == arbid2):
                                    xticks2.append(timestr)
                                    x2.append(count)
                                    y2.append(int(row[1]))

                            # Commit your changes in the database
                            db.commit()
                        except:
                            # Rollback in case there is any error
                            db.rollback()
                        # Now plot
                        self.plot2(x2, y2, xticks2, "INT", arbid2)

                # Frequency graph        
                if(g2fenable.get()):
                    if((current_ms_time() - last_time2) >= interval2):
                        sql = "SELECT * FROM LIVE_MON ORDER BY TS DESC LIMIT %d ;" % (p2fcount+1)

                        try:
                            # Execute the SQL command
                            cursor.execute(sql)
                            results = cursor.fetchall()

                            arbcount2 = 0

                            for row in results:
                                if(row[1] == arbid2):
                                    arbcount2 = arbcount2 + 1

                            # Commit your changes in the database
                            db.commit()
                        except:
                            # Rollback in case there is any error
                            db.rollback()
                        # Now plot
                        xticks2.append(str(current_ms_time()))
                        x2.append(frqcount2)
                        y2.append(arbcount2)
                        self.plot2(x2, y2, xticks2, "FRQ", arbid2)

                        frqcount2 = frqcount2 + 1
                        p2fcount = 0
                        last_time2 = current_ms_time()

            # Enable scrolling effect
            if(len(x1) > 20):
                del x1[0]
            if(len(y1) > 20):
                del y1[0]
            if(len(x2) > 20):
                del x2[0]
            if(len(y2) > 20):
                del y2[0]
            if(len(xticks1) > 20):
                del xticks1[0]
            if(len(xticks2) > 20):
                del xticks2[0]

            count = count + 1
            p1fcount = p1fcount + 1
            p2fcount = p2fcount + 1

            # If the stop button is pressed
            if stop == True:
                # Disconnect from server
                popen.kill()
                db.close()
                x1 = []
                x2 = []
                y1 = []
                y2 = []

            # Stop at desired packet capture count if enabled
            if numExists == True:
                if count >= num:
                    # Disconnect from server
                    popen.kill()
                    db.close()
                    x1 = []
                    x2 = []
                    y1 = []
                    y2 = []

    def adduptag(self, Ttree, TagEntry):
        newtag = TagEntry.get()
        checktag = False
        db = MySQLdb.connect("localhost","root","toor",self.VEHICLE_NAME )
        cursor = db.cursor()

        sql = "SELECT * FROM tags;"
        try:
            # Execute the SQL command
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                if(row[0] == newtag):
                    checktag = True
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        if(newtag != '' and checktag == False):
            sql = "INSERT INTO tags (ARB_ID) VALUES ('%s');" % (newtag)
            try:
                # Execute the SQL command
                cursor.execute(sql)
                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

            sql = "SELECT * FROM tags;"
            count = 0
            try:
                # Execute the SQL command
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    Ttree.insert("",count,values=(row), tags = ('tag',))
                    count = count + 1

                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

            db.close()


    def create_window_LiveMonitoring(self, x1, x2, y1, y2):

        if(self.VEHICLE_NAME == ""):
                self.TextArea.insert(END, "Please register/log in to a vehicle.\n")
                return

        global pa
        pa = Toplevel(root)
        pa.geometry("715x550+200+200")
        pa.wm_title("Live Monitoring")

        global iname
        iname = Entry(pa)
        iname.grid(row=0, column=3)
        iname.focus_set()

        Label(pa, text="CAN Interface Name:", width=25, relief=RAISED).grid(row=0, column=0)
        Label(pa, text="Total Packet Count (optional):", width=25, relief=RAISED).grid(row=2, column=0)

        global pcount
        pcount = Entry(pa)
        pcount.grid(row=2, column=3)
        pcount.focus_set()

        global TagEntry
        TagEntry = Entry(pa)
        TagEntry.grid(row=7, column=3, rowspan=1, columnspan=3, sticky=N+S+E+W)
        TagEntry.focus_set()

        addTag = Button(pa,text='Add Tag: ',command= lambda: self.adduptag(Ttree, TagEntry), height=1)
        addTag.grid(row=7, column=0, rowspan=1, columnspan=3, sticky=N+S+E+W)

        Label(pa, text="Top Live Plot", relief=RAISED, height=1).grid(row=11, column=0, columnspan=3, sticky=N+S+E+W)
        Label(pa, text="Bottom Live Plot:", relief=RAISED, height=1).grid(row=11, column=3, columnspan=3, sticky=N+S+E+W)

        # Create area for tag table
        canvas = Canvas(pa, borderwidth=0, background="#ffffff")
        #Textbox Frame
        frame = Frame(canvas, background="#ffffff")
        canvas.create_window((4,4), window=frame, anchor="w")

        canvas.grid(row = 4, column =0, rowspan = 3, columnspan = 6, sticky = N+S)
        frame.grid(row = 4, column =0, rowspan = 3, columnspan = 6, sticky = N+S)

        # Create column headers at the top and initialize cells
        Ttree = ttk.Treeview(canvas)
        Ttree["columns"]= ("TAGGED ARB ID's (RED)",)
        Ttree["show"] = "headings" # remove first empty column (id)

        # Initialize sizes of cells
        Ttree["height"] = 15
        for x in Ttree["columns"]:
            Ttree.column(x, width=400)
            Ttree.heading(x, text=x)

        # Declare labels for FILTERS, NEWEST MESSAGE, BYTE UPDATES
        Ttree.tag_configure('tag', background='red')
        Ttree.grid_rowconfigure(0, weight = 1)
        Ttree.grid_columnconfigure(0, weight = 1)
        Ttree.grid(sticky = (N,S))

        # Fill the table with current tags
        tagsexists = self.checkTrafficTable("tags")
        count = 0
        db = MySQLdb.connect("localhost","root","toor",self.VEHICLE_NAME)
        cursor = db.cursor()

        if(tagsexists):
            sql = "SELECT * FROM tags;"

            try:
                # Execute the SQL command
                cursor.execute(sql)
                results = cursor.fetchall()

                for row in results:
                    Ttree.insert("",count,values=(row), tags = ('tag',))
                    count = count + 1

                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()
        else:
            sql = "CREATE TABLE tags (ARB_ID CHAR(8))"
            try:
                # Execute the SQL command
                cursor.execute(sql)
                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

        db.close()

        # Add graph configuration options

        g1enabled = IntVar()
        g2enabled = IntVar()
        g1fenable = IntVar()
        g2fenable = IntVar()
        g1tenable = IntVar()
        g2tenable = IntVar()

        cg1 = Checkbutton(pa, text="Enable Top Graph", variable=g1enabled, onvalue=1, offvalue=0)#command= lambda: self.eng)
        cg1.grid(row=12, column=0, columnspan=3, sticky=N+S+E+W)
        cg2 = Checkbutton(pa, text="Enable Bottom Graph", variable=g2enabled, onvalue=1, offvalue=0)
        cg2.grid(row=12, column=3, columnspan=3, sticky=N+S+E+W)

        totalenable1 = Checkbutton(pa, text="Integral Mode", variable=g1tenable, onvalue=1, offvalue=0)
        totalenable2 = Checkbutton(pa, text="Integral Mode", variable=g2tenable, onvalue=1, offvalue=0)
        totalenable1.grid(row=13, column=0, columnspan=3, sticky=N+S+E+W)
        totalenable2.grid(row=13, column=3, columnspan=3, sticky=N+S+E+W)

        freqenable1 = Checkbutton(pa, text="Frequency Analysis Mode", variable=g1fenable, onvalue=1, offvalue=0)
        freqenable2 = Checkbutton(pa, text="Frequency Analysis Mode", variable=g2fenable, onvalue=1, offvalue=0)
        freqenable1.grid(row=14, column=0, columnspan=3, sticky=N+S+E+W)
        freqenable2.grid(row=14, column=3, columnspan=3, sticky=N+S+E+W)


        g1enabled.set(0)
        g2enabled.set(0)
        g1fenable.set(0)
        g2fenable.set(0)
        g1tenable.set(0)
        g2tenable.set(0)

        global ArbEntry1
        ArbEntry1 = Entry(pa)
        ArbEntry1.grid(row=15, column=1, rowspan=1, columnspan=1, sticky=N+S+E+W)
        ArbEntry1.focus_set()

        global ArbEntry2
        ArbEntry2 = Entry(pa)
        ArbEntry2.grid(row=15, column=4, rowspan=1, columnspan=1, sticky=N+S+E+W)
        ArbEntry2.focus_set()

        global FrqEntry1
        FrqEntry1 = Entry(pa)
        FrqEntry1.grid(row=16, column=1, rowspan=1, columnspan=1, sticky=N+S+E+W)
        FrqEntry1.focus_set()

        global FrqEntry2
        FrqEntry2 = Entry(pa)
        FrqEntry2.grid(row=16, column=4, rowspan=1, columnspan=1, sticky=N+S+E+W)
        FrqEntry2.focus_set()

        Label(pa, text="ARB ID", relief=RAISED, height=1).grid(row=15, column=0, columnspan=1, sticky=N+S+E+W)
        Label(pa, text="ARB ID", relief=RAISED, height=1).grid(row=15, column=3, columnspan=1, sticky=N+S+E+W)

        Label(pa, text="Time Interval (ms)(for frq)", relief=RAISED, height=1).grid(row=16, column=0, columnspan=1, sticky=N+S+E+W)
        Label(pa, text="Time Interval (ms)(for frq)", relief=RAISED, height=1).grid(row=16, column=3, columnspan=1, sticky=N+S+E+W)

        b = Button(pa,text='Start',command= lambda: self.startMon(g1enabled,g2enabled,g1fenable,g2fenable,g1tenable,g2tenable, x1, x2, y1, y2, ArbEntry1, ArbEntry2,FrqEntry1, FrqEntry2, iname, pcount))
        b.grid(row=17, column=1, columnspan=3, stick=N+S+E+W)

    def close_window(self):
        import sys
        sys.exit()

    def onFrameConfigure(self,canvas):
        # Reset the scroll region to fill the inner frame
        canvas.configure(scrollregion=canvas.bbox("all"))

    def startFuzz(self, B1, B2, B3, B4, B5, B6, B7, B8,RAND_ARB_en,CUST_ARB_en ,RAND_PKT_en ,CUST_PKT_en, ARB_FUZZ_NAME, iname, num):

        if(CUST_ARB_en.get() == 0):
            ARB_ID = ARB_FUZZ_NAME.get()
        else:
            ARB_ID = self.ARB_generator(3)


        if(CUST_PKT_en.get() == 0):
            cmd = "cansend %s %s#%s.%s%s.%s%s%s%s.%s" % (iname.get(),ARB_ID, B1.get(),B2.get(),B3.get(),B4.get(),B5.get(),B6.get(),B7.get(),B8.get())
        else:
            cmd = 'cansend %s %s#%s.%s%s.%s%s%s%s.%s' % (iname.get(),ARB_ID, self.ARB_generator(2),self.ARB_generator(2),self.ARB_generator(2),self.ARB_generator(2),self.ARB_generator(2),self.ARB_generator(2),self.ARB_generator(2),self.ARB_generator(2))
        pcount = num.get()

        even = 0
        for i in range(int(pcount)):
            if(CUST_PKT_en.get()):
                if(CUST_ARB_en.get()):
                    ARB_ID = self.ARB_generator(3)
                cmd = 'cansend %s %s#%s.%s%s.%s%s%s%s.%s' % (iname.get(),ARB_ID, self.ARB_generator(2),self.ARB_generator(2),self.ARB_generator(2),self.ARB_generator(2),self.ARB_generator(2),self.ARB_generator(2),self.ARB_generator(2),self.ARB_generator(2))
            for line in execute([cmd]):
                even = 1

    def launchfuzz(self, B1, B2, B3, B4, B5, B6, B7, B8,RAND_ARB_en,CUST_ARB_en ,RAND_PKT_en ,CUST_PKT_en, ARB_FUZZ_NAME, iname, num):
        thread = threading.Thread(target=self.startFuzz, args=(B1, B2, B3, B4, B5, B6, B7, B8,RAND_ARB_en,CUST_ARB_en ,RAND_PKT_en ,CUST_PKT_en, ARB_FUZZ_NAME, iname, num))
        thread.daemon = True
        thread.start()

    def ARB_generator(self, size, chars="ABCDEF12345678"):
        return (''.join(random.choice(chars) for _ in range(size)))

    def remove_gridobject(root, row, column):
        # remove from screen:
        for label in root.grid_slaves():
            if int(label.grid_info()["row"]) is row :
                if int(label.grid_info()["column"]) is column:
                    label.grid_forget()


root = Tk()
root.geometry("1158x1000+200+200")
root.configure(background='black')
app = Application(master=root)
app.mainloop()
