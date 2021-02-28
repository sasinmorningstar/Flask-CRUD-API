# -*- coding: utf-8 -*-

import sqlite3

DATABASE_NAME = "audioserver.db"


def get_db():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection

def create_tables():
    
    tables = [
        """
        CREATE TABLE IF NOT EXISTS song(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, duration INTEGER NOT NULL, uploadedTime INTEGER NOT NULL)
        
        """,
        """
        CREATE TABLE IF NOT EXISTS podcast(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, duration INTEGER NOT NULL, uploadedTime TEXT NOT NULL, host TEXT NOT NULL, participants TEXT)
        
        """,
        """
        CREATE TABLE IF NOT EXISTS audiobook(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, author TEXT NOT NULL, narrator TEXT NOT NULL, duration INTEGER NOT NULL, uploadedTime TEXT NOT NULL)
        
        """
        ]
    
    database = get_db()
    cursor = database.cursor()
    
    for table in tables:
        cursor.execute(table)