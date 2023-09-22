from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Authorid={self.id}, name={self.name})'
    
    @validates('name')
    def validate_name(self,key,value):
        if not value:
            raise ValueError("not possible")
        return value 
    
    
    @validates('phone_number')
    def validate_phone_number(self,key,value):
        if len(value) != 10:
            raise ValueError("not possible")
        return value


class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    
    category = db.Column(nullable=False)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
    @validates('title')
    def validate_title(self,key,value):
        if value not in ["Won't Believe","Secret","Top [number]","Guess"]:
            raise ValueError("not possible")
        return value
    @validates('content')
    def validate_content(self,key,value):
        if len(value) < 250:
            raise ValueError("not possible")
        return value
    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) > 250:
            raise ValueError("Post summary cannot exceed 250 characters.")
        return summary
    @validates('category')
    def validate_category(self,key,category):
        if category not in ["Fiction", "Non-Fiction"]:
            raise ValueError("not possible")
        return category

    
