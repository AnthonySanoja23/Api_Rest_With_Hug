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

def Todas_Las_Personas(num):
    if int(num) == 0:
        return Personas[0]
    elif int(num) == 1:
        return Personas[1]
    elif int(num) == 2:
        return Personas[2]
            
         
    


    