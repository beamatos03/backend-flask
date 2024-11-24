from flask_cors import CORS
from app import app

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}}, supports_credentials=True)



if __name__ == '__main__':
    app.run()
