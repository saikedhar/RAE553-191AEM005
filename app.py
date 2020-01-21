                                            # Flask class is imported 
from flask import Flask, request
                                        # abort, Resource, Api classes imported from flask_restful module 
from flask_restful import Resource, Api, abort, reqparse

                                #import JWT,jwt_required, current_identity from flask_jwt 
from flask_jwt import JWT, jwt_required, current_identity

                                        #import authenticate 
from security import authenticate, identity
from user import UserRegister
from item import Item

                # Flask application instance is created using below command
app = Flask(__name__)

                        # Adding a secreate line
app.secret_key = 'Saikedhar'

            #Api application instance is created 
api = Api(app)

            #create a JWT object.  Flask-JWT registers an with our application, /auth
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/<name>')
api.add_resource(UserRegister, '/signup')

if __name__ == '__main__':
    app.run(debug=True)
