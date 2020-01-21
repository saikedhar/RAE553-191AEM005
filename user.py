import sqlite3 # importing sqlite3
from flask_restful import Resource, reqparse

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    #adding price as argument
    parser.add_argument('username', type=str,required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str,required=True, help='This field cannot be left blank')

    #defining post to create users
    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return {"message":"A user with this username is already exists"}, 400
        connection = sqlite3.connect('data.db')
        cursor =   connection.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'],data['password']))

        connection.commit()
        connection.close()

        return {"message": "Awsome! User Created!!"}, 201

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    #verify the username exists in database
    @classmethod
    def find_by_username(cls, username):
        connection  = sqlite3.connect('data.db')
        cursor =   connection.cursor()

        query = "SELECT * FROM users WHERE username=?" #select every row in the database but uses only the data that matches parameter
        result = cursor.execute(query, (username,)) #since a single value tuple is necessary
        row = result.fetchone() #selects the first row out of the results set
        if row:
            #user = cls(row[0], row[1], row[2]) those match an id, username (index 1) and password (index2 ) respectfully
            user = cls(*row)
        else:
            user = None # None is when object doesnt exist
        
        connection.close()
        return user
    #verify the id exists in database
    @classmethod
    def find_by_id(cls, id):
        connection  = sqlite3.connect('data.db')
        cursor =   connection.cursor()

        query = "SELECT * FROM users WHERE id=?" #select every row in the database with given id
        result = cursor.execute(query, (id,)) #since a single value tuple is necessary
        row = result.fetchone() #selects the first row out of the results set
        if row:
            #user = cls(row[0], row[1], row[2]) those match an id,
            #  username (index 1) and password (index2 ) respectfully
            user = cls(*row)
        else:
            user = None # None is when object doesnt exist
        
        connection.close()
        return user
