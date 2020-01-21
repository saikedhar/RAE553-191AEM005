from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class student(Resource):
    def get(self, name):
        return {'student': name}

api.add_resource(student, '/student/<string:name>') 
app.run(port=5000)