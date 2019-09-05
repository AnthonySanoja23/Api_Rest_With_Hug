import hug 

import json

from pathlib import Path

my_file = Path("People.json")

people = []

authentication = hug.authentication.basic(hug.authentication.verify("Anthony", "1234"))

if my_file.exists():

	file = open("People.json", "r")
	data = file.read()
	file.close()
	People = json.loads(data)	


def save_in_json():

	data = json.dumps(People)
	f = open('People.json','w')
	f.write(data)
	f.close()


@hug.delete()
def delete_people(Person_id:int):
	global people

	for idx, Person in enumerate(people):
		if idx == Person_id:
			del people[idx]
			save_in_json() 
			break
	return people


@hug.put()
def update_people(Person_id:int,n,l,a):
	global people

	if len(people) - 1 >= Person_id:

		people[Person_id] = {'Name':n,'Last_Name':l,'Age':a}
		save_in_json()
			       
	return people       

@hug.post()
def add_person(n,l,a):
    global people
    people.append({'Name':n,'Last_Name':l,'Age':a})
    save_in_json()

    return people        



@hug.get('/people')
def get_people():
    global people
    return people

@hug.get('/people/{event}')

def find_person(Person_name):

	for Person in people:

		if Person['Name'] != Person_name:
			continue
		else:
			return Person['Name'],Person['Last_Name'],Person['Age']
  

# Authentication http     
@hug.get("/authentication", requires=authentication)
def basic_auth_api_call(user: hug.directives.user):
    return "Welcome: {0}".format(user)






    