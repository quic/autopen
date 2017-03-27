import matplotlib
matplotlib.use("TkAgg")
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation

import tkinter as tk   # python3
#import Tkinter as tk   # python
from tkinter import ttk


# Imports of custom - made helper classes
import dbUtils
import dataController
import carInterface
import createCarEntries
import katoolinAppsInstall
import sqlite3

# use ttk.Button instead of tk.Button

"""
Some notes
1. When adding pages, must add pages to list of pages. Will not automatically add.


"""


TITLE_FONT = ("Helvetica", 18, "bold")

class OpeningPage(tk.Tk):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "AutoPen")

        dbUtils

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # When you build new pages, add them to this list!
        # Otherwise they will not be visible to the controller
        self.pages = [StartPage, PageOne, PageTwo, PageThree, CreateCar, InstallModulesPage, LoadCar]

        #for F in (StartPage, PageOne, PageTwo, PageThree, CreateCar):
        for F in self.pages:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = ttk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = ttk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = ttk.Button(self, text="Go to Graphs page",
                            command=lambda: controller.show_frame("PageThree"))
        button4 = ttk.Button(self, text="Load Cars",
                             command=lambda :controller.show_frame("LoadCar"))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

        #buttonQuit = ttk.Button(self, text="Exit Program", command = quit())
        #buttonQuit.pack()




class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        button2 = ttk.Button(self, text = "Go to the create car Page", command=lambda: controller.show_frame("CreateCar"))
        button2.pack()



# Page class to create a car
class CreateCar(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        '''
        label = tk.Label(self, text="Car Manufacturer", font=TITLE_FONT).grid(row=2)
        label2 = tk.Label(self, text = "Car Model", font=TITLE_FONT).grid(row=3)
        label3 = tk.Label(self, text = "Car Year", font = TITLE_FONT).grid(row=4)

        #label.pack()
        #label2.pack()
        #label3.pack()

        #manuEntry =

        manufacturerEntry = tk.Entry(self, text="Manufacturer")
        manufacturerEntry.grid(row=2, column = 2)
        modelEntry = tk.Entry(self, text="Model")
        modelEntry.grid(row=3, column =2)
        yearEntry = tk.Entry(self, text="Year")
        yearEntry.grid(row=4, column = 2)

        print(manufacturerEntry.get())

        createCarEntries.createNewCarInDB(str(manufacturerEntry), str(modelEntry), str(yearEntry))

        #manuButton = tk.Button(self, text="Set Manu", command = manufacturerEntry.get())
        #manuButton.grid(row=2, column=3)
#
        #lolButton = tk.Button(self, text="print", command = print(manufacturerEntry.get()))
        #lolButton.pack()


        print("Let's get the manufacturer entry")
        print(manufacturerEntry.get())


        #print(manufacturerEntry)
        #print(modelEntry)
        #print(yearEntry)

        #button1 = tk.Button(self, text="show", command = manufacturerEntry.get, modelEntry.get, yearEntry.get)

    builder = ""
    model = ""
    year = ""

    #def getData(self):
        #self.year =



        #createCarEntries.createNewCarInDB(manufacturerEntry, modelEntry, yearEntry)


        #label.pack '''



# Class to load a car into the framework
class LoadCar(tk.Frame):
    print("nothing helper lolololo")



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Graph Page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        self.initialize()




        #var = StringVar(self)


        choices = {
        'Ford': '35',
        'Chevy': '45',
        'Lexus': '32',
        'Fucksus': '64',
        'Bullshit': '21',
        }



    # Code to build drop down menu
    # Please do not change
    # Theoretically should be broken but is working so far.
    def initialize(self):

        # Opening up the databse and interacting with it
        sqlite_file = 'carObjects.sqlite'
        table_name = 'cars'

        id_column = 'Make'
        some_id = 123456
        column_2 = 'Model'
        column_3 = 'Year'

        # Connecting to the database file
        conn = sqlite3.connect(sqlite_file)

        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM 'cars'")
            self.rows = cur.fetchall()
        #cur = conn.cursor()
        #print("Executing command")
        #cur.execute("SELECT * FROM Cars")
        #rows = cur.fetchall()

        for row in self.rows:
            print(row)




        # Dropdown Menu
        optionList = ["Yes","No"]
        self.dropVar=tk.StringVar()
        self.dropVar.set("Yes") # default choice
        self.dropMenu1 = tk.OptionMenu(self, self.dropVar, *optionList, command=self.func)
        self.dropMenu1.pack()
        print(self.dropVar)





    def func(self,value):
        print(value)



'''
Page where apps are installed.
Button to patch install all
or Button per singlular app
TODO resolve
'''
class InstallModulesPage(tk.Frame):
    print("nothing")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


# Graphs page
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Graph Page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        # Now we draw the graph

        #f = Figure(figsize=(5,5) dpi=100)
        f = Figure(figsize=(5,5), dpi=100)

        # add subplot
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8,9], [9,7,8,6,7,5,6,4,1])

        # Need to make a canvas, pack canvas into tkInter page.
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side = tk.TOP, fill=tk.BOTH, expand = True)

        # Create toolbar for graphing
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side = tk.TOP, fill=tk.BOTH, expand = True)
        #canvas.get_tk_widget().pack(side = tk.TOP, fill=tk.BOTH, expand = True)



if __name__ == "__main__":
    app = MainApp()
    app.mainloop()