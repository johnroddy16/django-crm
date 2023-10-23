import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'db_yug+61',
)

# prepare cursor object:

c = database.cursor()


# create the database:

c.execute('CREATE DATABASE IF NOT EXISTS usefulapps')

# a message for the terminal:

print('database created')