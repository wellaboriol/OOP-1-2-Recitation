import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Krizza Boriol\Documents\Database1.accdb;')
    print("Database is Connected")

    user_id=3
    Address = 'Cavite'
    database = connect.cursor()
    database.execute('update Table1 set Address=? where id=?',(Address,user_id))
    database.commit()
    print("Data is updated")

except pyodbc.Error:
    print("Error in Connection")