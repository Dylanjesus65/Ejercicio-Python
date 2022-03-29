'''
Escribir un programaque pida al usuario su peso (en kg) y estatura (en metros),
 calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase
"Tu índice de masa corporal es"(presentar el resultado con dos decimales)
'''
peso= float(input("Ingrese su peso en kg: "))
altura= float(input("Ingrese su altura en m: "))
imc= peso/altura**2
print("SU IMC ES: %3.2f "%imc)