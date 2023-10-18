from connect2 import * 


"""1. Print details of all films
2. Print all films of a particular genre
3. Print all films of a particular year
4. Print all films of a particular rating
5. Exit"""

def allRecords():
    dbCursor.execute("SELECT * FROM tblFilms")
    allRecords = dbCursor.fetchall()
    for eachRecord in allRecords:
        print(eachRecord)

    #create different functions to perform each task listed above

def genreSearch():
    genreValue = input("Enter Genre: ")
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genreValue}' ")
    genreRecords = dbCursor.fetchall()
    for eachRecord in genreRecords:
        print(eachRecord)


def yearSearch():
    yearValue = input("Enter Year: ")
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = '{yearValue}' ")
    yearRecords = dbCursor.fetchall()
    for eachRecord in yearRecords:
        print(eachRecord)


def ratingsSearch():
    ratingValue = input("Enter Ratings: ")
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{ratingValue}' ")
    ratingRecords = dbCursor.fetchall()
    for eachRecord in ratingRecords:
        print(eachRecord)



if __name__ == "__main__": 

   allRecords()
   genreSearch()
   yearSearch()
   ratingsSearch()

    
