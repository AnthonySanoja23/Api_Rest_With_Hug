import hug 
import json
from pathlib import Path
from configparser import ConfigParser
from falcon import *


parser = ConfigParser()
parser.read('../settings.ini')


authentication=parser.get('registry', 'authentication')

 
my_file = Path("People.json")

people = []




if my_file.exists():

	file = open("People.json", "r")
	data = file.read()
	file.close()
	people = json.loads(data)	



def save_in_json():

	data = json.dumps(people)
	f = open('People.json','w')
	f.write(data)
	f.close()


#Delete 
@hug.default_input_format("application/json")
@hug.delete('/delete/{Person_id}')
def delete_people(Person_id:int,response):
	global people

	for idx, Person in enumerate(people):
		if idx == Person_id:
			del people[idx]
			save_in_json() 
			break
			return (people)
		elif idx != Person_id:
			response.status == falcon.HTTP_204

			return 'The person is not registered'
				
			
#Update
@hug.default_input_format("application/json")
@hug.put('/update/{Person_id}/{n}/{l}/{a}')
def update_people(Person_id:int,n,l,a):
	global people

	if len(people) - 1 >= Person_id:

		people[Person_id] = {'Name':n,'Last_Name':l,'Age':a}
		save_in_json()

	else:
		return 'The person is not registered'	
			       
	return people


#Add person
@hug.default_input_format("application/json")
@hug.post('/add/{n}/{l}/{a}')
def add_person(n,l,a):
    global people
    people.append({'Name':n,'Last_Name':l,'Age':a})
    save_in_json()

    return people        


#List people
@hug.get('/people')
def get_people():
    global people

    return people


#Search person by id 
@hug.default_input_format("application/json")
@hug.get('/people/{Person_id}')
def find_person(Person_id:int):

	for idx, Person in enumerate(people):
		if idx == Person_id:

			return Person
		else:
			return 'The person is not registered'
			
  

# Authentication http     
@hug.get("/authentication", requires=authentication)
def basic_auth_api_call(user: hug.directives.user):
    return "Welcome: {0}".format(user)










    