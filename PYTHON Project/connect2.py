import sqlite3 as sql 

# To use the module, start by creating a database Connection object:
dbCon = sql.connect("/Users/rachelbenjamin/Documents/PYTHON Project/filmflix.db")

dbCursor = dbCon.cursor()