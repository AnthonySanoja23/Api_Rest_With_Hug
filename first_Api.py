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
def Personas():
    return Personas

@hug.get('/Personas1')
def First_Persona(''):
    return Personas[0]

@hug.get('/Persona2')

def Segunda_Persona():
    return Personas[1]

@hug.get('/Persona3')

def Tercera_Persona():
    return Personas[2]
    