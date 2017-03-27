import dbUtils
import time
import random
import datetime

dbName = "canData.db"
conn = dbUtils.createConnection(dbName)

i = 0
while i < 1000:
    time = str(datetime.datetime.now())
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    num3 = random.randint(1,50)
    num4 = random.randint(1,50)
    thing = []
    thing.append(time)
    thing.append(num1)
    thing.append(num2)
    thing.append(num3)
    thing.append(num4)
    print(thing)

    # conn = dbUtils.createConnection(dbName)
    dbUtils.createRandomCanTest(conn, thing)

    i+=1

conn.close()


