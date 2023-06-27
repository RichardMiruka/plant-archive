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

class User (Resource):
    def post(self):
        new_user = User(
            name = request.form['name'],
            updated_at = request.form['updated_at'],
            created_at =request.form['created_at'])
        
        db.session.add(new_user)
        db.session.commit()
        response_dict = new_user.to_dict()
        response = make_response(
            response_dict,
            201,
        )
        return response
api.add_resource(User, '/User')


        
        
        
if __name__ =='_main_':
   app.run(port=5555)