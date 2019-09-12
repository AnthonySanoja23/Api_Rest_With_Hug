import hug 
import json
from pathlib import Path
from configparser import ConfigParser

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




@hug.default_input_format("application/json")
@hug.delete('/delete/{Person_id}')
def delete_people(Person_id:int):
	global people

	for idx, Person in enumerate(people):
		if idx == Person_id:
			del Person[idx]
			save_in_json() 
			break
 
	return (hug.input_format.json(people))




@hug.default_input_format("application/json")
@hug.put('/update/{Person_id}/{n}/{l}/{a}')
def update_people(Person_id:int,n,l,a):
	global people

	if len(people) - 1 >= Person_id:

		people[Person_id] = {'Name':n,'Last_Name':l,'Age':a}
		save_in_json()
			       
	return (hug.input_format.json(people))



@hug.default_input_format("application/json")
@hug.post('/add/{n}/{l}/{a}')
def add_person(n:str,l:str,a:str):
    global people
    people.append({'Name':n,'Last_Name':l,'Age':a})
    save_in_json()

    return (hug.input_format.json(people))        



@hug.get('/people')
def get_people():
    global people
    return people


@hug.default_input_format("application/json")
@hug.get('/people/{Person_id}')
def find_person(Person_id:int):

	for idx, Person in enumerate(people):
		if idx == Person_id:
			return Person
			
  

# Authentication http     
@hug.get("/authentication", requires=authentication)
def basic_auth_api_call(user: hug.directives.user):
    return "Welcome: {0}".format(user)






    