from wit import Wit
from app import db
from models import Company, Events
access_token = 'ERIZHU2Q3IYPCEMCXKGEL3DZIR3RQN4A'

def processUserText(text):
    client = Wit(access_token=access_token)
    resp = client.message(text)
    return resp['entities']['filter'][0]['value']

def prepareReply(hasResult, all_result, resultType):
    reply = {}
    reply['hasResults'] = hasResult
    reply['results'] = all_result
    reply['resultType'] = 'place'
    reply['botReply'] = 'Query Complete. Showing ' + resultType + 'nearby'
    return reply

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
        dict_data['long'] = lng;
        dict_data['image'] = dict_data.pop('logo')
        dict_data['desc'] = dict_data.pop('description')
        all_results.append(dict_data)
    reply = prepareReply(hasResults, all_results)
    print reply
    return reply


def sendReply():
    keyword = processUserText('Could you find me places to eat');
    if keyword == 'restaurants and bar':
        return getRestaurants()
    return getEvents()
        
if __name__ == '__main__':
    sendReply()
