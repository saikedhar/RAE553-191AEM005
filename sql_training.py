import sqlite3
import random
import string
#creating database using connection
connection = sqlite3.connect('data.db')
# creatting a Cursor object 
cursor = connection.cursor()

#creating a TABLE
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# Inserting a row of static data with id as 1, username as Saikedhar
user = (1, 'Saikedhar', 'Saikedhar2737')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

connection.commit() 

# defining function called dynamic_user_entry for generating credentials  
def dynamic_user_generate(num):
    name = ''.join([random.choice(string.ascii_uppercase) for n in range(6)]) #random upper case letter with lenght of 6
    pas = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range(10)])     #password includes uppercase, lowercase and number
    cursor.execute("INSERT INTO users (id, username, password) VALUES (?, ?, ?)", (num, name, pas)) # Inserting the values into table
    connection.commit() 

for i in range(2,6):
    dynamic_user_generate(i)

for row in cursor.execute('SELECT * FROM users ORDER BY id'):
    print(row)


connection.close()
