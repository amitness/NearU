from wit import Wit
from app import db
from models import Company, Events
import json
access_token = 'ERIZHU2Q3IYPCEMCXKGEL3DZIR3RQN4A'

def processUserText(text):
    client = Wit(access_token=access_token)
    resp = client.message(text)
    return resp['entities']['filter'][0]['value']

def prepareReply(hasResult, all_result, resultType):
    reply = {}
    reply['hasResults'] = hasResult
    reply['results'] = all_result
    reply['botReply'] = 'Query Complete. Showing results'
    return json.dumps(reply)

def getRestaurants():
    restaurants = db.session.query(Company).filter_by(org_type='Restaurant').all()
    hasResults = len(restaurants)>0
    all_results = []
    for restaurant in restaurants:
        location, lat, lng = restaurant.location.split(',')
        dict_data = restaurant.__dict__
        dict_data.pop('_sa_instance_state')
        dict_data.pop('location')
        dict_data['location'] = location
        dict_data['lat'] = lat;
        dict_data['resultType'] = 'place'
        dict_data['long'] = lng;
        dict_data['image'] = dict_data.pop('logo')
        dict_data['desc'] = dict_data.pop('description')
        all_results.append(dict_data)
    return hasResults, all_results

def getEvents():
    events = db.session.query(Events).all()
    hasResults = len(events)>0
    all_events = []
    for event in events:
        location, lat, lng = event.location.split(',')
        eventDict = event.__dict__
        eventDict.pop('location')
        eventDict['location'] = location
        eventDict['lat'] = lat
        eventDict['long'] = lng
        eventDict['resultType'] = 'event'
        eventDict.pop('_sa_instance_state')
        eventDict['image'] = eventDict.pop('banner')
        all_events.append(eventDict)
    return hasResults, all_events

def sendReply(userText):
    keyword = processUserText(userText)
    if keyword == 'restaurants and bar':
        has_result, result = getRestaurants()
    elif keyword == 'event' or keyword=='events':
        has_result, result = getEvents()
    #elif keyword == 'none':
    else:
        has_result1, result1 = getEvents() 
        has_result2, result2 = getRestaurants()
        has_result = has_result1 or has_result2
        result = result1 + result2
    
    reply = prepareReply(has_result, result, keyword)
    return reply

def getEventByID(event_id):
    events = db.session.query(Events).filter_by(id=event_id).all()
    hasResults = len(events)>0
    all_events = []
    for event in events:
        location, lat, lng = event.location.split(',')
        eventDict = event.__dict__
        eventDict.pop('location')
        eventDict['location'] = location
        eventDict['lat'] = lat
        eventDict['long'] = lng
        eventDict['resultType'] = 'event'
        eventDict.pop('_sa_instance_state')
        eventDict['image'] = eventDict.pop('banner')
        all_events.append(eventDict)
    return prepareReply(hasResults, all_events, 'event')

def getRestaurantsByID(r_id):
    restaurants = db.session.query(Company).filter_by(id=r_id).all()
    hasResults = len(restaurants)>0
    all_results = []
    for restaurant in restaurants:
        location, lat, lng = restaurant.location.split(',')
        dict_data = restaurant.__dict__
        dict_data.pop('_sa_instance_state')
        dict_data.pop('location')
        dict_data['location'] = location
        dict_data['resultType'] = 'place'
        dict_data['lat'] = lat;
        dict_data['long'] = lng;
        dict_data['image'] = dict_data.pop('logo')
        dict_data['desc'] = dict_data.pop('description')
        all_results.append(dict_data)
    return prepareReply(hasResults, all_results, 'restaurant')

if __name__ == '__main__':
    sendReply('find restaurants nearby')
