print("calculadora")
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))
num3 = int(input("ingrese otro numero: "))
while True:    
    print("menu de opciones")
    print("1. sumar")
    print("2. restar")
    print("3. dividir")
    print("4. multipiclar")
    opc = int(input("ingrese una opcion: "))
    if opc == 1:
        print("la suma es: ", num1 + num2 + num3)
        break
    elif opc == 2:
        print("la resta es: ", num1 - num2 - num3)
        break
    elif opc == 3:
        print("la division es: ", num1 / num2 / num3)
        break
    elif opc == 4:
        print("la multiplicacion es: ", num1 * num2 * num3)
        break
    