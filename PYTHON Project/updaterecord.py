#import module to update data from songs table.
from connect2 import *

# create function 
def update_data():
    # use primary key to update a record

    idField = input("Enter tableID of the record to be updated")

    #field to be updated
    fieldName = input("Enter title or yearReleased or rating or duration or genre as field name").title()

    # field value : ask for the for the Title or or yearReleased or rating or duration or genre to be updated
    fieldValue = input(f"Enter the value for the {fieldName} field")

    fieldValue = "'"+fieldValue+"'"   #  add single quotes around the field value (string)

    # update record
    dbCursor.execute(F"UPDATE films SET {fieldName} = {fieldValue} WHERE filmID = {idField}")

    dbCon.commit()

    print(f"Record {idField} updated in the films table")




if __name__ == "__main__":
    update_data()
