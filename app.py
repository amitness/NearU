from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
# import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/cb_core_db'
db = SQLAlchemy(app)


class Company(db.Model):
    __table__name = "Company"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    location = db.Column(db.String(255))
    description = db.Column(db.Text)
    org_type = db.Column(db.String(20))
    logo = db.Column(db.String(100))

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __repr__(self):
        return '<Company %r>' % self.name


class Events(db.Model):
    __tablename__ = "Events"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    location = db.Column(db.String(255))
    dateTime = db.Column(db.DateTime)
    description = db.Column(db.Text)
    organizer = db.Column(db.Integer, db.ForeignKey('company.id'))
    banner = db.Column(db.String(1000))

    def __init__(self, title, location):
        self.title = title
        self.location = location

    def __repr__(self):
        return '<Event %r>' % self.title


class Reviews(db.Model):
    __tablename__ = "Reviews"
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    rating = db.Column(db.Float)
    eventID = db.Column(db.Integer, db.ForeignKey('Events.id'))

    def __init__(self, comment, rating, eventID):
        self.comment = comment
        self.rating = rating
        self.eventID = eventID


class Landmark(db.Model):
    __tablename__ = "Landmarks"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(20))
    description = db.Column(db.Text)
    image = db.Column(db.String(1000))

    def __init__(self, location, description, image):
        self.location = location
        self.description = description
        self.image = image


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/response', methods=['POST'])
def response():
    # print requests;
    return jsonify({'text': 'response will go here'})


@app.route('/chatbox')
def chatbox():
    return render_template('chatbox.html')

if __name__ == '__main__':
    print db
    db.create_all()
    app.run(host='0.0.0.0', port=8000, debug=True)
