from datetime import datetime, timedelta
from app import app
import jwt
from flask import jsonify, request
from functools import wraps
import bcrypt

from app.users import user_by_email

def auth():
    

    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({
            'message': 'Nâo foi possível validar',
            'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    
    user = user_by_email(auth.username)
    
    
    if not user:
        return jsonify({'message': 'Usuario não encontrado'}), 401
        
    if user and bcrypt.checkpw(auth.password.encode('utf-8'), user['senha']):
       
        token = jwt.encode({'email': user['email'], 'exp': datetime.now() + timedelta(hours=12)},
                           app.config['SECRET_KEY'])
        
        return jsonify({
        'email': user['email'],
        'name': user['nome'],
        'surname':user['sobrenome'],
        'message': 'Validado com sucesso', 
        'token': token,
        'exp': datetime.now() + timedelta(hours=12)
                        
        })
    
    return jsonify({
            'message': 'Não foi possível validar',

            'WWW-Authenticate': 'Basic auth="Login required'}), 401