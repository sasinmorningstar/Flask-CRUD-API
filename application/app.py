# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import game_controller, audioserver
from database import create_tables

app = Flask(__name__)



@app.route('/<audioFileType>', methods=["GET"])
def get_audiofiles(audioFileType):
    audiofiles = audioserver.get_audiofiles(audioFileType)
    
    return jsonify(audiofiles)



@app.route("/<audioFileType>/<audioFileID", methods=["GET"])
def get_audiofile_by_id_type(audioFileType, audioFileID):
    
    audiofile = audioserver.get_by_id_type(audioFileID, audioFileType)
    
    return jsonify(audiofile)




# @app.route("/game", methods=["POST"])
# def insert_game():
#     game_details = request.get_json()
#     name = game_details['name']
#     price = game_details['price']
#     rate = game_details['rate']
#     result = game_controller.insert_game(name, price, rate)
    
#     return jsonify(result)


# @app.route("/game", methods=["PUT"])
# def update_game():
#     game_details = request.get_json()
#     id = game_details['id']
#     name = game_details['name']
#     price = game_details['price']
#     rate = game_details['rate']
#     result = game_controller.update_game(id, name, price, rate)
    
#     return jsonify(result)



@app.route("/<audioFileType>/audioFileID>", methods=["DELETE"])
def delete_data(audioFileType, audioFileID):
    result = audioserver.delete_data(audioFileType, audioFileID)
    
    return jsonify(result)








if __name__=="__main__":
    create_tables()
    
    app.run(host='0.0.0.0', port=8000, debug=False)




