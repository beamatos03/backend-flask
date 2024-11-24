from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] ='recovery.bluelotus@gmail.com'
app.config['MAIL_PASSWORD'] = 'bwzb vunt ytna cpno'
mail=Mail(app)

from .routes import routes
