
while True:
    try:
        op1=(float(input("dime el primer numero: ")))
        break
    except ValueError:
        print("el valor introducido no es un numero. Prueba de nuevo")

while True:
    try:
        op2=(float(input("dime el segundo numero: ")))
        break
    except ValueError:
        print("el valor introducido no es un numero. Prueba de nuevo")

operacion=input("que operacion quieres hacer? (suma, resta, multiplicación, división, elevado) ")

#defino las operaciones
def sume(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicación(num1,num2):
    return num1*num2

def división(num1,num2):
    try:
        return num1/num2
    
    except ZeroDivisionError:
        print("no se puede dividir entre 0")


def elevado(num1,num2):
    return num1^num2

#operamos la calculadora

if operacion=="suma":
    print(sume(op1,op2))

elif operacion=="resta":
    print(resta(op1,op2))

elif operacion=="multiplicación":
    print(multiplicación(op1,op2))

elif operacion=="división":
    print(división(op1,op2))

else: 
    print("WIP")

print("Esto es todo amigos")