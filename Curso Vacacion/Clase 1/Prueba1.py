'''
Solicitará el nombre al usuario y lo guardará en una variable denominada ‘nombre’
Solicitará el primer apellido al usuario y lo guardará en una variable denominada ‘apellido’
Almacenaremos en una nueva variable denominada ‘fullName’,
el nombre y apellido registrado separados por un espacio.
Además, se solicitará su año de nacimiento y lo guardará en una variable denominada ‘anio’
Calcularemos y asignaremos a una nueva variable ‘edad’ la edad el usuario
'''
from datetime import datetime
nombre=str(input("Escriba su nombre"))
apellido=str(input("Escriba su apellido"))
anio=int(input("Ingrese el anio"))
edad=2022-anio
print("LA edad ES",edad)
print("Y TE LLAMAS "+str(nombre)+""+str(apellido))