#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:15:49 2021

@author: somitsinha
"""

# Devspace

from datetime import datetime
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

   
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime, default=datetime.now)












    
@app.route('/<audioFileType>/', methods=['GET','POST'])
def get_insert_data(audioFileType):
    
    if request.method=='GET':
        if audioFileType=='Song':
            songs = Song.query.all()
          
            return render_template('list.html', songs=songs)
    
    
    
    
    if request.method=='POST':
        if audioFileType=='Song':
            data = request.get_json()
            name = data['name']
            duration = data['duration']
            # upload_time = data['upload_time']
            
            song = Song(name=name, duration=duration)
            
            db.session.add(song)
            db.session.commit()
        
            return '<h1>Action is successful: 200 OK</h1>'



@app.route('/<audioFileType>/<audioFileID>', methods=['GET','PUT','DELETE'])
def get_update_delete_data(audioFileType, audioFileID):
    
    
    
    if request.method=='GET' and audioFileType=='Song':
        song = Song.query.filter_by(id=audioFileID).first()
        
        return f'<h1>Song name is { song.name } and runtime is { song.duration }</h1>'
    
    
    
    
    if request.method=='PUT' and audioFileType=='Song':
        data = request.get_json()
        
        song = Song.query.filter_by(id=audioFileID).first()
        
        song.name = data['name']
        song.duration = data['duration']
        
        db.session.commit()
        
        return '<h1>Song data updated successfully 200:OK</h1>'
    

    
    if request.method=='DELETE' and audioFileType=='Song':
        data = Song.query.filter_by(id=audioFileID).first()

        db.session.delete(data)
        db.session.commit()

        return '<h1>Audio Data deleted successfully: 200 OK</h1>'



# import requests
# put = requests.put('http://localhost:5000/Song/4', json={"name":"Human Nature", "duration":"720s"})

# put.status_code


# import requests
# post = requests.post('http://localhost:5000/Song', json={"name":"Cry", "duration":"450s"})

# post.status_code


# import requests
# delete = requests.delete('http://localhost:5000/Song/4')

# delete.status_code



if __name__=="__main__":
    # db.create_all()
    app.run()



























