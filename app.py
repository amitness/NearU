import os
from flask import Flask, render_template, jsonify
from models import db
import chatbot
# import requests
# import json

app = Flask(__name__)

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')

DATABASE_URI = 'mysql+pymysql://{}:{}@localhost:3306/cb_core_db'
DATABASE_URI = DATABASE_URI.format(DB_USERNAME, DB_PASSWORD)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

# Initialize SQLAlchemy
db.app = app
db.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/response', methods=['POST'])
def response():
    # print requests;
    return jsonify({'text': 'Check the map.'})

@app.route('/event/<id>')
def event(id):
    return chatbot.getEventByID(id)

@app.route('/place/<id>')
def place(id):
    return chatbot.getRestaurantsByID(id)

if __name__ == '__main__':
    print db
    #db.create_all()
    app.run(host='0.0.0.0', port=8000, debug=True)
