import sqlite3 #It's necessary import sqlite and json
import json

def dict_factory(cursor, row): #This is to add to the JSON the description of each table's field
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect("ApiJsonDB") #Creating conection to the DB
conn.row_factory = dict_factory
cursor = conn.cursor()

# fetch all or one we'll go for all.
cursor.execute('select * from json') # Selecting all table's registers
results = cursor.fetchall()

with open('sqlite_file_db.json', 'w') as json_file: #Creating the file in the main folder
	json.dump(results, json_file, indent=4)

conn.close() #closing the conection
