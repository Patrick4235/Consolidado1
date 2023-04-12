def suma(a,b):
    resultado=a+b
    return print("el resultado es: "+resultado)

def resta(a,b):
    resultado=a-b
    return print("el resultado es: "+resultado)

def multiplicacion(a,b):
    resultado=a*b
    return print("el resultado es: "+resultado)

def divicion(a/b):
    resultado=a+b
    return print("el resultado es: "+resultado)

Num1 = input("ingrese el primer numero: ")
Num2 = input("ingrese el primer numero: ")

operacion = input("escriba el numero de la operacion a realisar: \n 1.- suma \n 2.- Resta \n 3.- multiplicacion \n 4.- divicion \n Coloque numero: ")

if operacion == 1:
    suma(Num1,Num2)

elif operacion ==2:
    resta(Num1,Num2)
    
elif operacion ==3:
    multiplicacion(Num1,Num2)
    
elif operacion ==4:
    divicion(Num1,Num2)
    