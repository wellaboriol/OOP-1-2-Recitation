import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Krizza Boriol\Documents\Database1.accdb;')
    print("Database is Connected")


except pyodbc.Error:
    print("Error in Connection")