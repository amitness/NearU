from wit import Wit
from app import db
from models import Company, Events
access_token = 'ERIZHU2Q3IYPCEMCXKGEL3DZIR3RQN4A'

def processUserText(text):
    client = Wit(access_token=access_token)
    resp = client.message(text)
    return resp['entities']['filter'][0]['value']


if __name__ == '__main__':
    processUserText('Could you find me places to eat');
