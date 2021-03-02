
from flask import Flask, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
# import json

# Initialize sql-alchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    db.init_app(app)

    


    # app = create_app()
    
    from app.models import Song
    
    @app.route('/', methods=['GET'])
    def server_status():
        response = jsonify(Server="Running")
        response.status_code = 200
        
        return response


    
    @app.route('/<audioFileType>/', methods=['GET','POST'])
    def get_insert_data(audioFileType):
        
        if request.method=='GET':
            if audioFileType=='Song':
                songs = Song.query.all()
                results = []
                
                for song in songs:
                    _object = {
                        'id': song.id,
                        'name': song.name,
                        'duration': song.duration,
                        'upload_time': song.upload_time
                        }
                    results.append(_object)
                
                response = jsonify(results)
                response.status_code = 200
                return response
        
        
        
        
        if request.method=='POST':
            if audioFileType=='Song':
                data = request.json
                # name = data['name']
                name = str(data.get('name'))
                # duration = data['duration']
                duration = str(data.get('duration'))
                # upload_time = data['upload_time']
                
                song = Song(name=name, duration=duration)
                
                db.session.add(song)
                db.session.commit()
                
                response = jsonify({
                    'id': song.id,
                    'name': song.name,
                    'duration': song.duration,
                    'upload_time': song.upload_time
                    })
                response.status_code = 201
            
                return response



    @app.route('/<audioFileType>/<audioFileID>', methods=['GET','PUT','DELETE'])
    def get_update_delete_data(audioFileType, audioFileID):
        
        
        
        if request.method=='GET' and audioFileType=='Song':
            song = Song.query.filter_by(id=audioFileID).first()
            
            response = jsonify({
                'id': song.id,
                'name': song.name,
                'duration': song.duration,
                'upload_time': song.upload_time
                })
            response.status_code = 200
            
            return response
    
    
    
    
        if request.method=='PUT' and audioFileType=='Song':
            data = request.json
            
            song = Song.query.filter_by(id=audioFileID).first()
            
            song.name = data['name']
            song.duration = data['duration']
            
            db.session.commit()
            
            response = jsonify({
                'name': song.name,
                'duration': song.duration
                })
            response.status_code = 200
            
            return response
    

    
        if request.method=='DELETE' and audioFileType=='Song':
            data = Song.query.filter_by(id=audioFileID).first()
    
            db.session.delete(data)
            db.session.commit()
    
            return {
                "message": "song {} deleted successfully".format(audioFileID)
                }, 200
        
    return app
