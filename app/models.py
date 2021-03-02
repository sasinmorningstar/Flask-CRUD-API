# -*- coding: utf-8 -*-

from datetime import datetime
from app import db

class Song(db.Model):
    
    '''This class represents the song table'''
    # __tablename__ = 'Song'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime, default=datetime.now)
    
    
    # def __init__(self, name):
    #     '''initialize with name'''
    #     self.name = name
        
    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()
        
    # @staticmethod 
    # def get_all():
    #     return Song.query.all()
    
    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()