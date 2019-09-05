import hug 

import json

from pathlib import Path

my_file = Path("People.json")

People = []

autenticacion = hug.authentication.basic(hug.authentication.verify("Anthony", "1234"))

if my_file.exists():

	archive = open("People.json", "r")
	datos = archive.read()
	archive.close()
	Personas = json.loads(datos)	




def guardar_en_json():

	datos = json.dumps(People)
	f = open('People.json','w')
	f.write(datos)
	f.close()


@hug.delete()
def borrar_Personas(Persona_id:int):
		global Personas

		for idx, Persona in enumerate(Personas):
				if idx == Persona_id:
						del Personas[idx]
						guardar_en_json() 
						break
		return Personas


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






    