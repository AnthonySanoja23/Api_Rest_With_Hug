import hug 

import json

from pathlib import Path

my_file = Path("Personas.json")

Personas = []


if my_file.exists():

	archivo = open("Personas.json", "r")
	datos = archivo.read()
	archivo.close()
	Personas = json.loads(datos)	

else:

	print("No hay data cargada debido a que el archivo no existe ")
	input("Presione una tecla para continuar")


def guardar_en_json():

	datos = json.dumps(Personas)
	f = open('Personas.json','w')
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
        

		else:
			 print('La persona no esta registrado en la lista ')

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
    


    