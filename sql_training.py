import sqlite3
import random
import string

connection = sqlite3.connect('data.db')#creating data.db database using connection(connect)
cursor = connection.cursor()# creatting a Cursor object and call its execute() method to perform SQL commands

#creating a TABLE
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# Inserting a row of static data with id as 1, username as Saikedhar
user = (1, 'Saikedhar', 'Saikedhar2737')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

connection.commit() # Save (commit) the changes

# defining function called dynamic_user_entry for generating credentials  as per the task
def dynamic_user_generate(num):
    name = ''.join([random.choice(string.ascii_uppercase) for n in range(6)]) #random upper case letter with lenght of 6
    pas = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range(10)])     #password includes uppercase, lowercase and number
    cursor.execute("INSERT INTO users (id, username, password) VALUES (?, ?, ?)", (num, name, pas)) # Inserting the values into table
    connection.commit() # save the changes

for i in range(2,6):# calling dynamic_user_generate to generate random credentials 
    dynamic_user_generate(i)

for row in cursor.execute('SELECT * FROM users ORDER BY id'):#printing all the numbers with sorting id
    print(row)

# close the connection
connection.close()
