#importar libreria
import os

# definicion de operaciones
def suma(a,b):
    resultado=a+b
    return resultado

def resta(a,b):
    resultado=a-b
    return resultado

def multiplicacion(a,b):
    resultado=a*b
    return resultado

def divicion(a,b):
    resultado=a/b
    return resultado

#ingreso de datos para ejecutar operaciones
Num1 = float(input("ingrese el primer numero: "))
Num2 = float(input("ingrese el primer numero: "))

#menu de ejecuciones
operacion = 1
while operacion > 0 or operacion < 5:

    operacion = int (input("escriba el numero de la operacion a realisar: \n 1.- suma \n 2.- Resta \n 3.- multiplicacion \n 4.- divicion \n 5.- Salir \n Coloque numero: "))

    if operacion == 1:
        print(f"el resultado es: {suma(Num1,Num2)}")
        os.system("pause")
        os.system("cls")
    
    elif operacion == 2:
        print(f"el resultado es: {resta(Num1,Num2)}")
        os.system("pause")
        os.system("cls")
    
    elif operacion == 3:
        print(f"el resultado es: {multiplicacion(Num1,Num2)}")
        os.system("pause")
        os.system("cls")
    
    elif operacion == 4:
        print(f"el resultado es: {divicion(Num1,Num2)}")
        os.system("pause")
        os.system("cls")

    elif operacion == 5:
        break