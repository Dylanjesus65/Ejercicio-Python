'''
Se necesita elaborar un algoritmo que solicite el número de respuestas correctas, incorrectas de una prueba,
y muestre su puntaje final junto con el equivalente en porcentaje de aciertos y errores
'''
rcorrectas=int(input("Numero de respuestas correctas"))
rincorrectas=int(input("Numero de respuestas incorrectas"))
total=rcorrectas+rincorrectas
porcentajebueno=(100/total)*rcorrectas
porcentajemalo=(100/total)*rincorrectas
print("TIENE :",rcorrectas," Correctas,",rincorrectas," Respuestas incorrectas de un total de ",total," preguntas")
print("El porcentaje bueno es de :%.2f El porcentaje malo es de : %.2f "%(porcentajebueno,porcentajemalo))
