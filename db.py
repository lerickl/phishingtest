import sqlite3

conext = sqlite3.connect("appdatabase.sqlite")

cursor = conext.cursor()
sql_query= """ CREATE TABLE usuario (
    id integer PRIMARY KEY,
    name text NOT NULL,
    email text NOT NULL,
    password text NOT NULL
)"""
sql_query1= """ CREATE TABLE busquedaNew (
    id integer PRIMARY KEY,
    url text NOT NULL 
)"""

cursor.execute(sql_query)
cursor.execute(sql_query1)