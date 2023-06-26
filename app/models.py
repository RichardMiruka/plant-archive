from flask_sqlalchemy import SQLAlchemy

from sqlalchemy_serializer import SerializerMixin 

db = SQLAlchemy()
class User(db.Model,SerializerMixin):
    __tablename__='users'
    id= db.Column('id',db.Integer(),primary_key=True)
    name = db.Column("name",db.String())
    serialize_rules=('-plant.user')
    plants=db.relationship('Plant', backref= 'user')
    
    created_at = db.Column('created_at', db.DateTime, default=db.func.now())
    updated_at = db.Column('updated_at', db.DateTime, onupdate=db.func.now())
    
class Plant(db.Model, SerializerMixin):
    __tablename__="plants"
    id = db.Column('id',db.Integer(),primary_key=True)
    user_id = db.Column('user_id',db.Integer(),db.ForeignKey('users.id'))
    plant_type = db.Column('plant_type', db.String())
    serialize_rules=('-user.plants')
    
    created_at = db.Column('created_at', db.DateTime, default=db.func.now())
    updated_at = db.Column('updated_at', db.DateTime, onupdate=db.func.now())
    
    
          