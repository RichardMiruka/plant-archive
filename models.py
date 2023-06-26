from flask_sqlalchemy import SQLAlchemy
from app import app

from sqlalchemy_serializer import SerializerMixin 

db = SQLAlchemy()
class User(db.Model,SerializerMixin):
    __tablename__='users'
    id= db.Column('id',db.Integer(),primary_key=True)
    name = db.Column("name",db.String())
    serialize_rules=('-plant.user')
    
    created_at = db.Column('created_at', db.Datetime, default=db.func.now())
    updated_at = db.Column('updated_at', db.Datetime, onupdate=db.func.now())
    
class Plant(db.Model, SerializerMixin):
    __tablename__="plants"
    id = db.Column('id',db.Integer(),primary_key=True)
    user_id = db.Column('user_id',db.Integer(),db.ForeignKey('users.id'))
    plant_type = db.Column('plant_type', db.string())
    serialize_rules=('-user.plants')
    
    
          