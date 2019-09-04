import hug 

import json

from pathlib import Path

my_file = Path("Personas.json")

Personas = []


if my_file.exists():

	archivo = open("Personas.json", "r")
	datos = archivo.read()
	archivo.close()
	clientes = json.loads(datos)	

else:

	print("No hay data cargada debido a que el archivo no existe ")
	input("Presione una tecla para continuar")


def guardar_en_json():

	datos = json.dumps(clientes)
	f = open('Personas.json','w')
	f.write(datos)
	f.close()





@hug.put()
def actualizar_Persona(Persona_id,actr_Persona):
		global Personas

		if len(Personas) - 1 >= Persona_id:
				Personas[Persona_id] = actr_Persona

				guardar_en_json()

		else:
			 print('La persona  no esta registrado en la lista ')




@hug.post()
def Agregar_Persona(n,a,e):
    Personas.append({'Nombre':n,'Apellido':a,'Edad':e})


    return Personas        



@hug.get('/Personas')
def Mostrar_Personas():
    return Personas

@hug.get('/Personas/{event}')
def Todas_las_personas(event: int):
    if event == 0:
        return Personas[0]    
    elif event == 1:
        return Personas[1]
    elif event == 2:
        return Personas[2]    
    


    