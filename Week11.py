import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = ('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)''')
cursor.execute(create_table)


users =[
    (1, 'Saikedhar', '5678'),
    (2, 'jan', '8976'),
    (3, 'uppala', '4567')
]

insert_query = ("INSERT INTO users VALUES (?, ?, ?) ")
for i in users:
    cursor.execute(insert_query, (i))

connection.commit()

connection.close()
print(users)