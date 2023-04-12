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

try: 
    Num1 = float(input("ingrese el primer numero: "))
    Num2 = float(input("ingrese el primer numero: "))
except ValueError:
        print("SOLO SE ACEPTAN NUMEROS")



operacion = int (input("escriba el numero de la operacion a realisar: \n 1.- suma \n 2.- Resta \n 3.- multiplicacion \n 4.- divicion \n Coloque numero: "))

if operacion == 1:
    print(f"el resultado es: {suma(Num1,Num2)}")
        
elif operacion == 2:
    print(f"el resultado es: {resta(Num1,Num2)}")
    
elif operacion == 3:
    print(f"el resultado es: {multiplicacion(Num1,Num2)}")
    
elif operacion == 4:
    try:
        print(f"el resultado es: {divicion(Num1,Num2)}")
    except ZeroDivisionError:
        print("NO SE PUEDE DIVIDIR POR CERO")
