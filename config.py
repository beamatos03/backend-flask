import string
import random

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))

DEBUG = True
SECRET_KEY = key
FRONTEND_URL = "http://localhost:4200"




