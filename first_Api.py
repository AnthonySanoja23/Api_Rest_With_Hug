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



@hug.get('/Personas/{event}')
def Todas_las_personas(event: int):
    if event == null:
        return Personas
    elif event == 0:
        return Personas[0]    
    elif event == 1:
        return Personas[1]
    elif event == 2:
        return Personas[2]    
    


    