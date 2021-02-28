#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:24:04 2021

@author: somitsinha
"""

from database import get_db




def insert_data(name, price, rate):
    database = get_db()
    cursor = database.cursor()
    statement = "INSERT INTO games(name, price, rate) VALUES (?, ?, ?)"
    cursor.execute(statement, [name, price, rate])
    database.commit()
    
    return True



def insert_data(audioFileType, ):
    database = get_db()
    cursor = database.cursor()
    
    if audioFileType=="song":
        query = "INSERT INTO song(id, name, duration, uploadedTime) VALUES (?,?,?,?)"
        # cursor.execute(query)













def update_data(id, name, price, rate):
    database = get_db()
    cursor = database.cursor()
    statement = "UPDATE games SET name=?, price=?, rate=? WHERE id=?"
    cursor.execute(statement, [name, price, rate, id])
    database.commit()
    
    return True


def delete_data(id):
    database = get_db()
    cursor = database.cursor()
    statement = "DELETE FROM games WHERE id=?"
    cursor.execute(statement, [id])
    database.commit()
    
    return True


# def get_by_id(id):
#     database = get_db()
#     cursor = database.cursor()
#     statement = "SELECT id, name, price, rate FROM games WHERE id=?"
#     cursor.execute(statement, [id])
    
#     return cursor.fetchone()

def get_by_id_type(_id,_type):
    database = get_db()
    cursor = database.cursor
    query = "SELECT * from type=? WHERE id=?"
    cursor.execute(query, [_type, _id])
    
    return cursor.fetchone()


# def get_games():
#     database = get_db()
#     cursor = database.cursor()
#     query = "SELECT id, name, price, rate FROM games"
#     cursor.execute(query)
    
#     return cursor.fetchall()
    
def get_audiofiles(audioFileType):
    database = get_db()
    cursor = database.cursor()
    query = f'SELECT * from {audioFileType}'
    cursor.execute(query)
    
    return cursor.fetchall()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    