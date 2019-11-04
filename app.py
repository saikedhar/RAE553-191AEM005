# abort, Resource, Api classes imported from flask_restful module inorder to create the first rest api
from flask_restful import Resource, Api, abort

from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity

# Flask application instance is created using below command
app = Flask(__name__)

# Adding a secreate line
#app.config['SECRET_KEY'] = 'FirstJson1'
app.secret_key = 'FirstJson1'

#Api application instance is created using below command
api = Api(app)

jwt = JWT(app, authenticate, identity)

#defining total items
items = {}

@@ -18,19 +27,22 @@
class item(Resource):
    # GET method to print an specific item
    # if the requted item doesnt exist, it will abort with an error with code 404
    @jwt_required()
    def get(self, name):
        if name in items:
            return {name: items[name]}
        else:
            abort(404, message="{} doesn't exist".format(name))

    #put method to create a new item or modify the existing
    @jwt_required()
    def put(self, name):
        items[name] = {'price' : request.form['price'] }
        return {name: items[name]}

    # POST method to create a new endpoint with concrete price value as requested.
    # if the requted name already exist, it will abort and  print an error with error code 403
    @jwt_required()
    def post(self, name):
        if name not in items:
            items[name] = { 'price' : '500' }
@@ -39,6 +51,7 @@ def post(self, name):
            abort(403, message="{} exist".format(name))
    # DELETE method to DEleTE an specific item
    # if the requted item doesnt exist, it will abort with an error with code 404
    @jwt_required()
    def delete(self, name):
        if name in items:
            del items[name]
@@ -51,12 +64,14 @@ def delete(self, name):
# get method to print all the items

class itemList(Resource):
    @jwt_required()
    def get(self):
        return items

##
##  setup the Api resources routing
##

api.add_resource(item, '/items/<name>')
api.add_resource(itemList, '/items')

 21  security.py 
@@ -0,0 +1,21 @@
# importing safe_str_cmp from werkzeug to compare strings
from werkzeug.security import safe_str_cmp
from user import User

#creating Users list
users = [
    User(1, 'naresh', 'naresh1234'),
    User(2, 'bandaru', 'bandaru1234'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None) 
 5  user.py 
@@ -0,0 +1,5 @@
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
