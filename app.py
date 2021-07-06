from flask import Flask, request, jsonify
from flask_cors import CORS
#import torch
import numpy as np
from PIL import Image
import sqlite3
from conexion import conex
import json 
from buscarMetadatosUrl import buscarMetadatosurl
#import pickle
app = Flask(__name__)
CORS(app)
conn = conex()

#conn.db_conexion()


@app.route('/AnalizarUrl', methods=['POST'])
def buscarUrl():
    if request.method == 'POST':
        url = request.json['url'] 
        #loaded_model = pickle.load(open('Model_phishing.pkl', 'rb'))
        #result = loaded_model.predict(url)
        #print(result)
   
        return jsonify([{"Result": url}]) 

@app.route('/buscarUrl', methods=['POST'])
def buscarUrl():
    if request.method == 'POST':
        url = request.json['url'] 
        buscar = buscarMetadatosurl(url) 
        tempTITLE=buscar.Obtener_TITLE()
        tempDESCRIPCION=buscar.Obtener_Descripcion()
         
        return jsonify([{"titulo": tempTITLE,"descripcion": tempDESCRIPCION}]) 

@app.route('/')
def hello_world():
    return 'Hello, World!'
# Create Data Routes

@app.route('/urls',methods=['GET','POST']) 
def urlsGETPOST():
    connex = conex()
    if request.method == 'GET':
        return jsonify(connex.get_news())
    if request.method == 'POST':  
        new_url = request.json['url']      
        connex.post_news(new_url)
        return f"busqueda creada", 201
@app.route("/urls/<int:id>", methods=["GET","PUT","DELETE"])
def urlsGETPUTDELETE(id):
    connex = conex()    
    if request.method == "GET":                        
        return jsonify(connex.get_new(id))  
    if request.method == "PUT":
        id = request.json["id"]
        url = request.json["url"]      
        connex.put_url(id,url)
        update_url = {
            "id": id,
            "url": url
        }   
        return jsonify(update_url)
    if request.method == "DELETE":       
        return jsonify(connex.delete_new(id)), 200    

@app.route('/users',methods=['GET','POST']) 
def usersGETPOST():
    connex = conex()    
    if request.method == 'GET':
       return jsonify(connex.get_users())  
    
    if request.method == 'POST':         
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']       
        return jsonify(connex.post_user(name, email, password))
@app.route('/users/<int:id>', methods=["GET","PUT","DELETE"])   
def usersGETPUTDELETE(id):
    return True
    
  
"""
    new_product = {
       'url': request.json['url']
    } 
    listnews.append(new_product)
    return jsonify({'message':'noticia agregada'})"""

@app.route("/predict", methods=['POST'])
def predict():
 
    return {
        print("api funcionando")
    }

if __name__ == "__main__":
    app.run(debug=True)