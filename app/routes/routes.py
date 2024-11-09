from app import app, users
from flask import jsonify

from app.views import auth

@app.route("/", methods=['GET'])
def home():
    return('API funciona')

@app.route("/register", methods=['POST'])
def registerUser():
    return users.registerUser()

@app.route("/update/<id>", methods=['PUT'])
def updateUser(id):
    return users.updateUser(id)

@app.route("/delete/<id>", methods=['DELETE'])
def deleteUser(id):
    return users.deleteUser(id)

@app.route("/auth", methods=['POST'])
def authenticate():
    return auth.auth()