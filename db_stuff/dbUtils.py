import sqlite3
from sqlite3 import Error
import os


##############################################
#       FIRST CHECK TO SE IF DB EXISTS
#############################################

# Database Names
generalDBName = "autoPenGeneralData.sqlite"
testDBName = "testDB.sqlite"


# Temporary variables to store existance of databse.
generalDBExists = not os.path.exists(generalDBName)
testDBExists = not os.path.exists(testDBName)



#########
# INIT #
########

def init():
        # First check to see if database already exists.
        print("nothing")



########################################################################
# Function definitions to build databases if they do not already exists#
########################################################################

# Method to build the general purpose database
def generalDBBuild():
        dbConn = sqlite3.connect(generalDBName)
        c = dbConn.cursor()

def testDBBuild():
        testDbConn = sqlite3.connect(testDBName)
        testCuror = testDbConn.cursor()



############################################################
# Function to create DB for a car and function to add to it#
############################################################

def createDBforCar(dbName, tableName):
        print("Nothing~")

def addToCarDB(dbName, tableName, timestsamp, canField):
        print("Nothing")






###################################
# Function to add user to program #
###################################

def addUser(firstName, lastName, userName):
        print("nothing")






# REAL STUFF

def createConnection(dbFile):

        """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
        # print("about to try and open DB")
        try:
                conn = sqlite3.connect(dbFile)
                # print("Opened DB")
                return conn

        except Error as e:
                print(e)


        return None

def selectAllCars(conn):
        print("Inside selectallcars")

        cur = conn.cursor()
        cur.execute("SELECT * FROM cars")
        # print("executed cursor")
        rows = cur.fetchall()
        return rows


def createCar(conn, car):
        print("creating car")

        sql = "INSERT INTO cars(Make, Model, Year) VALUES(?,?,?)"
        cur = conn.cursor()
        #cur.execute(sql, car)
        cur.execute("INSERT INTO cars VALUES(?,?,?)", car)
        print("ran execute code")
        #cur.commit()
        conn.commit()
        print(cur.lastrowid)


def createRandomCanTest(conn, item):
        cur = conn.cursor()
        cur.execute("INSERT INTO Ford_Taurus_Test VALUES(?,?,?,?,?)",item)
        conn.commit()








# GARBAGE - DELETE LATER!
#############################################

# sqlite_filename = "autoPenData.sqlite"
#
# db_is_new = not os.path.exists(sqlite_filename)
#
# print("Inside the dbutils helper method")




# sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
# table_name1 = 'my_table_1'  # name of the table to be created
# table_name2 = 'my_table_2'  # name of the table to be created
# new_field = 'my_1st_column' # name of the column
# field_type = 'INTEGER'  # column data type

# db_is_new1 = not os.path.exists(sqlite_file)
#
# if db_is_new1:
#         conn = lite.connect(sqlite_file)
#         c = conn.cursor()
#
#         c.execute('CREATE TABLE {tn} ({nf} {ft})'\
#                 .format(tn=table_name1, nf=new_field, ft=field_type))
#
#         # Creating a second table with 1 column and set it as PRIMARY KEY
#         # note that PRIMARY KEY column must consist of unique values!
#         c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
#                 .format(tn=table_name2, nf=new_field, ft=field_type))
#
#         conn.commit()
#         conn.close()
#
#
#
# # Connecting to the database file
# conn = lite.connect(sqlite_file)
# c = conn.cursor()
#
#
# # Committing changes and closing the connection to the database file
# conn.commit()
# conn.close()