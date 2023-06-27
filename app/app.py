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
#index
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

#get-user


#post-user
class Users(Resource):
    def post(self):
        new_user = User(
            name = request.form['name']
            # updated_at = request.form['updated_at'],
            # created_at =request.form['created_at']
            )
        db.session.add(new_user)
        db.session.commit()
        response_dict = new_user.to_dict()
        response = make_response(
            jsonify(response_dict),
            201,
        )
        return response
api.add_resource(Users, '/users')

#delete-user and patch-user
class UserID(Resource):
    def delete(self, id):
        user=User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return "", 204
        else:
            response_dict={
                "message": 'no user'
            }
            response = make_response(
                jsonify(response_dict), 404
            )
            return response

    def patch(self, id):
        user = User.query.get(id)
        

        if user:
                for attr in request.form:
                  setattr(user,attr,request.form.get(attr))
                db.session.add(user)
                db.session.commit()

                user_dict= user.to_dict()

                response = make_response(
                    jsonify(user_dict), 200
                )

                return response
        else:
                response_dict={
                "message": 'no user'
               }
                response = make_response(
                jsonify(response_dict), 404
               )
                return response

api.add_resource(UserID,'/users/<int:id>')    








#post-plant


class Plants(Resource):
   def post(self):
    new_plant = Plant(
    user_id=request.form['user_id'],
    plant_type = request.form['plant_type']
    # updated_at = request.form['updated_at'],
    # created_at =request.form['created_at']
    )
    db.session.add(new_plant)
    db.session.commit()
    response_dict = new_plant.to_dict()
    response = make_response(
    jsonify(response_dict),
    201,
    )
    return response

   def get(self):
       plants=[plant.to_dict() for plant in Plant.query.all()]
       return make_response(jsonify(plants),200)

    


api.add_resource(Plants, '/plants')








#delete-plant and patch-plant



    
if __name__ =='_main_':
   app.run(port=5000)










































