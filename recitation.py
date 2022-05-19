import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Krizza Boriol\Documents\Database1.accdb;')
    print("Database is Connected")

    database = connect.cursor()
    database.execute('''INSERT INTO Table1 (ID, FullName, Age, Address, Birthdate, SemGrade) VALUES (11, 'Boriol,Wella Mae', '20', 'Cavite', '08/05/2002', 95)''')
    database.commit()
    print('User was successfully added')

except pyodbc.Error:
    print("Error in Connection")