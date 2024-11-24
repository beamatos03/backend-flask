from app import app, users
from flask import jsonify, request, url_for

from app.models.models import User
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

@app.route("/auth", methods=['GET','POST'])
def authenticate():
    return auth.auth()

@app.route("/reset_password", methods=["POST"])
def reset_pass():
    data = request.get_json()
    email = data['email']
    return users.send_reset_password_email(email)

@app.route("/reset_password/newPassword/<token>", methods=["PUT"])
def reset_token(token):
    try:
        # Verifica o token
        user = User.verify_token(token)
        if not user:
            return jsonify({'error': 'Token inválido ou expirado', 'error': 'Falha na verificação do token'}), 400
        update_result = updateUser(user)
        if not update_result:
            return jsonify({'error': 'Erro ao atualizar a senha', 'error': 'Falha na função updateUser'}), 500
        
        else:
            return jsonify({'message': 'Senha atualizada com sucesso'}), 200

    except Exception as e:
        print(f"Erro inesperado ao processar a solicitação: {e}")
        return jsonify({'message': 'Erro interno no servidor', 'error': str(e)}), 500
