from app import db, Events, Company, Landmark, Reviews
import pandas

def insert_events():
	event_data = pandas.read_csv('events.csv')
	for i in range(len(event_data)):
		event = Events(event_data['title'][i], 
				event_data['location'][i],
				event_data['dateTime'][i],
				event_data['description'][i],
				event_data['organizer'][i],
				event_data['banner'][i])
		db.session.add(event)
	db.session.commit()
#Insert hotels/shops
def insert_company():
	companies = pandas.read_csv('events.csv')
	for i in range(len(companies)):
		company = Company(event_data['title'][i], 
				event_data['location'][i],
				event_data['dateTime'][i],
				event_data['description'][i],
				event_data['organizer'][i],
				event_data['banner'][i])
		db.session.add(event)
	db.session.commit()
