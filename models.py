from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

db = SQLAlchemy(app)
Migrate(app, db)

class UploadInfo(db.Model):

    __tablename__ = 'uploadInfo'

    id = db.Column(db.Integer,primary_key = True)
    message_type = db.Column(db.String(20) ,nullable = False)
    user_name = db.Column(db.String(50) , nullable = False)
    upload_date = db.Column(db.DateTime, nullable = False)
    json = db.Column(db.Text, nullable = False)
    message = db.Column(db.Text)
    filename = db.Column(db.String(100))
    filepath = db.Column(db.LargeBinary)

    def __init__(self,message_type,user_name,upload_date,json,message,filename,filepath):
        self.message_type = message_type
        self.user_name = user_name
        self.upload_date = upload_date
        self.json = json
        self.message = message
        self.filename = filename
        self.filepath = filepath

