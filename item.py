
from flask_restful import Resource, Api, abort, reqparse
from flask_jwt import JWT, jwt_required, current_identity

import sqlite3


class Item(Resource):
    TABLE_NAME = 'items'
    parser = reqparse.RequestParser()
    parser.add_argument('cost', type=float,required=True, help='Please fill me')
    # GET method to Get an specific item
    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message':'Item not found check the error'}, 404
    # POST method to Post an specific item
    @jwt_required()
    def post(self, name):
        if self.find_by_name(name):
            return {"message": "An item with name '{}' already Present".format(name)}
        data = Item.parser.parse_args()
        item = {'name': name, 'cost':data['cost']}
        try:
            Item.insert(item)
        except:
            return {"message":"An error occured during inserting item"}, 500
        return item, 201
        # PUT method to put an specific item
    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        update_item = {'name': name, 'cost':data['cost']}
        if item is None:
            try:
                Item.insert(update_item)
            except:
                return {"message":"an error occured during update an item"}
        else:
            try:
                Item.update(update_item)
            except:
                raise
                return {"message":"an error occured during update an item"}
        return update_item

    # To finding the item in the list
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME) # verify if it exist
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'item': {'name':row[0], 'cost':row[1]}} #return the exist item

   
    @classmethod
    def insert(cls, item):
    
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
       
        query = "INSERT INTO {table} VALUES (?,?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['name'],item['cost']))
        connection.commit() #commit and close the db access
        connection.close()
        return {'message':'Item Added Successfully'}   

    #update method for PUT methods
    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE {table} SET cost=? WHERE name=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['cost'],item['name']))
        connection.commit()
        connection.close()
        return {'message':'Item Updated Successfully'}   
    #DELETE METHOD
    @jwt_required()
    def delete(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'message':'Item Deleted successfully'}   

