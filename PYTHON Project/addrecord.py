#import module to add data to films table.
from connect2 import *

def insert_data():
    

    filmTitle = input("Enter the title: ")
    year_released = int(input("Enter the year released: "))
    filmRating = input("Enter the rating: ")
    filmDuration = int(input("Enter the duration (in minutes): "))
    filmGenre = input("Enter the genre: ")

#create cursor
        
    dbCursor.execute("INSERT INTO tblfilms(Title, yearReleased, Rating, Duration, Genre) VALUES(?, ?, ?, ?, ?)", (filmTitle, year_released, filmRating, filmDuration, filmGenre))
    dbCon.commit() #used to permanently write data in the film table of the database.

if __name__ == "__main__":
    insert_data()