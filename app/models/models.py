from itsdangerous import BadSignature, BadTimeSignature, SignatureExpired, URLSafeTimedSerializer as Serializer
import jwt
from app import app, users


class User():

    def get_token(email, password):
        serial = Serializer(app.config["SECRET_KEY"])
        return serial.dumps(email, salt=password)
    
    @staticmethod
    def verify_token(token_id):
        token, user_id = token_id.split('usuario_')
        serial=Serializer(app.config["SECRET_KEY"])
        user = users.user_by_id(user_id)
        password = user['senha']
        # Tenta desserializar o token
        try:
            user_email = serial.loads(token, max_age=300, salt=password)
            print(f"E-mail do usuário extraído do token: {user_email}")
            # Retorna o e-mail do usuário se tudo estiver correto
            return users.user_by_email(user_email)['_id']
        except Exception as e:
            return None
