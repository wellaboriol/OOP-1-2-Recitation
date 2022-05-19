import pyodbc

msa_drivers = [x for x in pyodbc.drivers() if 'access']
print(f'Access Drivers: {msa_drivers}')


