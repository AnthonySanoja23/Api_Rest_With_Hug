import hug 

import json

from pathlib import Path

my_file = Path("People.json")

people = []

autenticacion = hug.authentication.basic(hug.authentication.verify("Anthony", "1234"))

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
def delete_people(Persona_id:int):
		global people

		for idx, Persona in enumerate(people):
				if idx == Persona_id:
						del people[idx]
						guardar_en_json() 
						break
		return people


@hug.put()

def actualizar_Personas(Persona_id:int,n,a,e):
		global Personas

		if len(Personas) - 1 >= Persona_id:
				Personas[Persona_id] = {'Nombre':n,'Apellido':a,'Edad':e}

				guardar_en_json()
        
	

		return Personas       

@hug.post()
def Agregar_Persona(n,a,e):
    global Personas
    Personas.append({'Nombre':n,'Apellido':a,'Edad':e})
    guardar_en_json()

    return Personas        



@hug.get('/Personas')
def Mostrar_Personas():
    global Personas
    return Personas

@hug.get('/Personas/{event}')

def Todas_las_personas(event: int):
    global Personas
    if event == 0:
        return Personas[0]    
    elif event == 1:
        return Personas[1]
    elif event == 2:
        return Personas[2]    

# Autenticacion por http     
@hug.get("/Auntenticacion", requires=autenticacion)
def basic_auth_api_call(usuario: hug.directives.user):
    return "Bienvenido: {0}".format(usuario)






    