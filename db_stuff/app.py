import tkinter as tk   # python3
import operator
import sqlite3
import dbUtils
#import Tkinter as tk   # python

TITLE_FONT = ("Helvetica", 18, "bold")

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        pagesList = [StartPage, LoadCarPage, CreateCarPage, LoadDataPage]
        for F in (pagesList):
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
        label = tk.Label(self, text="Welcome to AutoPen!", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Load Car Page",
                            command=lambda: controller.show_frame("LoadCarPage"))
        button2 = tk.Button(self, text="Create Car Page",
                            command=lambda: controller.show_frame("CreateCarPage"))
        button1.pack()
        button2.pack()


class LoadCarPage(tk.Frame):


    #Helper method to load the list of cars from the database.
    def loadListOfCars(self):
        print("nothing")

        db_conn = sqlite3.connect("carObjects.sqlite")
        cursor = db_conn.cursor()

    def switchToNextPage(self, carName, controller):
        temp = carName.split()
        self.carName = "_".join(temp)
        print(self.carName)
        controller.show_frame("LoadDataPage")

    def getCarName(self):
        return self.carName



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Load Car", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        dbFile = "carObjects.sqlite"

        conn = dbUtils.createConnection(dbFile)
        dbUtils.selectAllCars(conn)

        rows = dbUtils.selectAllCars(conn)
        #print(type(rows))

        carsList = []
        tempo = ""

        for row in rows:
            option = " ".join(row)
            carsList.append(option)

        print(carsList)

        self.carName = ""




        listOfCars = ["Chicken", "Egg", "Milk"]

        variable = tk.StringVar(self)
        variable.set(carsList[0]) # default value

        drop = tk.OptionMenu(self, variable, *carsList)
        drop.pack()

        executeButton = tk.Button(self, text="Load", command=lambda: self.switchToNextPage(variable.get(), controller))
        executeButton.pack()


class CreateCarPage(tk.Frame):

    def setcontents(self, make, model, year):
        self.makeString = make
        self.modelString = model
        self.yearString = year
        self.cars.append(make)
        self.cars.append(model)
        self.cars.append(year)

        print(self.cars)
        self.fullName = make + " " + model + " " + year

        # print(self.makeString,self.modelString,self.yearString, self.fullName)

    def getContents(self, make, model, year):
        info = [make, model, year]
        return info

    def executeDBevent(self):
        db_conn = sqlite3.connect('carObjects.sqlite')
        theCursor = db_conn.cursor()

        try:
            db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INT NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")
            db_conn.commit()
        except sqlite3.OperationalError:
            print("Table could not be created")



        db_conn.close()


    def insertCar(self):
        dbFile = "carObjects.sqlite"
        conn = dbUtils.createConnection(dbFile)
        dbUtils.createCar(conn, self.cars)


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Create Car Page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        ment = tk.StringVar()
        makeEnt = tk.Entry(self)
        makeLabel=tk.Label(self, text="Make", font=TITLE_FONT)
        makeLabel.pack()
        makeEnt.pack()


        modelEnt = tk.Entry(self)
        modelLabel = tk.Label(self, text="Model", font=TITLE_FONT)
        modelLabel.pack()
        modelEnt.pack()


        yearEnt =tk.Entry(self)
        yearLabel = tk.Label(self, text="Year", font=TITLE_FONT)
        yearLabel.pack()
        yearEnt.pack()


        self.makeString= ""
        self.modelString= ""
        self.yearString= ""
        self.fullName=""

        self.cars = []


        b1 = tk.Button(self, text="Create Car", command = lambda: self.setcontents(makeEnt.get(),modelEnt.get(), yearEnt.get()))
        b1.pack()

        b2 = tk.Button(self, text="Execute DB Call", command = lambda : self.insertCar())
        b2.pack(side="bottom")



class LoadDataPage(tk.Frame):


    # The car name is equivalent to the table name which is to be used later on.
    def loadData(self):
        self.carName = LoadCarPage.getCarName()
        print(self.carName)


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Load Car", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        self.carName = ""

        button = tk.Button(self, text="Buffer Data", command=lambda: self.loadData())
        button.pack()




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()