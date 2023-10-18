# import the connect.py module to read data from the film table
from connect2 import *

# create function 
def delete_data():
        # use primary key to delete a record
        idField = input("Enter the filmID of the record to be deleted: ")

        # delete from the field where the filmid is 1/2/3/4/5......
        dbCursor.execute(f"DELETE FROM title WHERE filmID = {idField}")
        dbCon.commit()

        print(f"Record {idField} deleted from the film table")
if __name__ == "__main__":
        delete_data()


