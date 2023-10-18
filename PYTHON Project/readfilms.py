#import module to read data from songs table.
from connect2 import *

def read_data():

    #select all record from songs table
    dbCursor.execute("SELECT * FROM tblFilms")

    #fetch the selected record
    allRecords = dbCursor.fetchall()

    # loop through and display all records
    for eachRecord in allRecords:
        print(eachRecord)

if __name__ == "__main__":
    read_data()

  
