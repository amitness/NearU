import os
import json
from flask import Flask, render_template, jsonify
from models import db
import chatbot
# import requests

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
    dummy_response = {
        'hasResults': True,
        'results': [
            {
                'title': 'Event Name',
                'desc': 'description',
                'lat': 27.67410,
                'long': 85.31710,
                'location': 'location',
                'image': 'image location',
                'resultType': 'event/place'
            }
          ],
        'botReply': 'Reply from bot.'
    }
    return jsonify(dummy_response)


@app.route('/event/<id>')
def event(id):
    details = chatbot.getEventByID(id)
    details = json.loads(details)
    result = details['results'][0]
    return render_template('events.html', result=result)


@app.route('/place/<id>')
def place(id):
    details = chatbot.getRestaurantsByID(id)
    details = json.loads(details)
    result = details['results'][0]
    return render_template('place.html', result=result)

if __name__ == '__main__':
    print db
    # db.create_all()
    app.run(host='0.0.0.0', port=8000, debug=True)
