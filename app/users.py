from flask import Flask, jsonify, request, make_response, session
#import jwt
from datetime import datetime, timedelta
import bcrypt
from dotenv import load_dotenv, find_dotenv
import os
import pymongo
from bson import ObjectId
from flask_cors import CORS

load_dotenv(find_dotenv())

app = Flask(__name__)
app.secret_key = "testing"
passwordDB = os.environ.get("MONGODB_PWD")

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}}, supports_credentials=True)
connection_string = f"mongodb+srv://FatecItu:{passwordDB}@fatecitu.zqencgi.mongodb.net/"

# Criando um client
client = pymongo.MongoClient(connection_string)

try:
    database = client.blue_lotus
    collection = database.get_collection("usuarios")
    print("Conectado ao MongoDB")

except Exception as e:
    # imprimir mensagem de erro em caso de falha na conexão
    print(f"Erro: {e}")

#CRUD
def registerUser():
    data = request.json
    name = data['name']
    surname = data['surname']
    phone = data['phone']
    email = data['email']
    password1 = data['password1']
    password2 = data['password2']
    gender = data['gender'],
    birthDate = data['birthDate']

    
    emailExists = collection.find_one({"email": email})

    if emailExists:
        return jsonify({'error': 'Este e-mail já está em uso.'}), 400
    if password1!=password2:
        return jsonify({'error': 'Senhas não coincidem.'}), 400 

    #criptografia da senha
    #genSalt => impede que 2 senhas iguais tenham resultados iguais
    hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())


    usuarios_document ={
        "nome": name,
        "sobrenome": surname,
        "email": email,
        "telefone": phone,
        "senha":  hashed_password,
        "genero": gender,
        "data_nasc": birthDate}
    try:
        insert_id = collection.insert_one(usuarios_document).inserted_id
        return jsonify({'message': 'Usuário registrado com sucesso', 'insert_id': str(insert_id)}), 201
    except:
        return jsonify({'message': 'Não foi possível registrar', 'insert_id': str(insert_id)}), 500

def updateUser(id):
    data = request.json
    name = data['name']
    surname = data['surname']
    phone = data['phone']
    email = data['email']
    password1 = data['password1']
    password2 = data['password2']
    gender = data['gender'],
    birthDate = data['birthDate']

    user = collection.find_one({'_id': ObjectId(id)})

    if not user:
        return jsonify({'message': "Usuário não existe"}), 404
    
        
    emailExists = collection.find_one({"email": email})

    if emailExists:
        return jsonify({'error': 'Este e-mail já está em uso.'}), 400
    if password1!=password2:
        return jsonify({'error': 'Senhas não coincidem.'}), 400 

    #criptografia da senha
    #genSalt => impede que 2 senhas iguais tenham resultados iguais
    hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())


    usuarios_document ={
        "nome": name,
        "sobrenome": surname,
        "email": email,
        "telefone": phone,
        "senha":  hashed_password,
        "genero": gender,
        "data_nasc": birthDate}
    
    
    try:
        insert_id = collection.update_one({'_id': ObjectId(id)}, {'$set': usuarios_document})
        return jsonify({'message': 'Usuário atualizado com sucesso', 'insert_id': str(insert_id)}), 201
    except:
        return jsonify({'message': 'Não foi possível registrar', 'insert_id': str(insert_id)}), 500

def deleteUser(id):
    user = collection.find_one({'_id': ObjectId(id)})

    if not user:
        return jsonify({'message': "Usuário não existe"}), 404
    
    try:
        delete_id = collection.delete_one({'_id': ObjectId(id)})
        return jsonify({'message': 'Usuário removido com sucesso'}), 201
    except:
        return jsonify({'message': 'Não foi possível remover'}), 500



def login():
    data = request.json
    email = data['email']
    password = data['password']

    
    emailExists = collection.find_one({'email': email})
    if not emailExists:
        return jsonify({'error': 'Credenciais inválidas'}), 401
    if not bcrypt.checkpw(password.encode('utf-8'), emailExists['senha']):
        return jsonify({'error': 'Credenciais inválidas'}), 401
    return jsonify({'message': 'Login bem-sucedido', 'user_id': str(emailExists['_id'])}), 200

if __name__ == '__main__':
    app.run(debug=True)


def user_by_email(email):
    try:
        return collection.find_one({"email": email})
    except:
        return None