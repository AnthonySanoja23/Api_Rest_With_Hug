import hug 



Personas=[
         {'Nombre':'Anthony',
         'Apellido':'Sanoja',
         'Edad':'23'},

         {'Nombre':'Alejandro',
         'Apellido':'Ortegano',
         'Edad':'26'},

         {'Nombre':'Cesar',
         'Apellido':'Rivas',
         'Edad':'24'},

         ]

@hug.get('/Personas')
    return Personas


def First_Persona():
    return Personas[0]

@hug.get('/Persona2')

def First_Persona():
    return Personas[1]

@hug.get('/Persona3')

def First_Persona():
    return Personas[2]
    