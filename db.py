import pyodbc 
# Some other example server values are
# server = 'sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'sqlserver.database.windows.net' 
database = 'db name' 
username = 'service acc' 
password = 'password123' 
trusted_connection = 'no'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+ ';trusted_connection =' +trusted_connection)
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';trusted_connection ='+trusted_connection)
cursor = cnxn.cursor()
#Sample select query
query = "insert into tablename (column1, column2) values(123,'get')"
#cursor.execute("SELECT * from tablename") 
cursor.execute(query)
#cursor.commit()



'''row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()'''