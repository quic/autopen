import sqlite3 as lite
import os



# Method to interact with our databse of cars
def createNewCarInDB(manu, model, year):

    databaseName = "carObjects.sqlite"
    carDBExists = not os.path.exists(databaseName)



    tableName = "listOfCars"

    connection = lite.connect(databaseName)
    cursor = connection.cursor()

    item = [manu, model, year]

    command = "insert into " + tableName + " values " + "(" + manu + "," + model + "," + year + ")"
    print(command)

    #cursor.execute(command)
    cursor.execute('insert into listOfCars values (?,?,?)', item)
    connection.commit()
    connection.close()

#createNewCarInDB("Ford", "Taurus", "1994")




