from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
from models import db, Plant, User
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api =Api(app)

    
        
db.init_app(app)

migrate = Migrate(app, db)
class Index (Resource):
   def get(self):
       response_dict={
           'Status':'success',
           "message": "Welcome to the API"
       }
       response = make_response(
           jsonify(response_dict
        
           ),
           200,
           
       )
       return response
api.add_resource(Index,'/')  
        
if __name__ =='_main_':
   app.run(port=5555)