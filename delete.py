import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Krizza Boriol\Documents\Database1.accdb;')
    print("Database is Connected")

    user_id=11
    database = connect.cursor()
    database.execute('delete from Table1 where id=?',(user_id))
    database.commit()
    print("record is deleted")


except pyodbc.Error:
    print("Error in Connection")