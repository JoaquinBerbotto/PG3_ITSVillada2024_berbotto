try:
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    resu = num1 / num2
    print("Tu calculo da", resu)
except ZeroDivisionError:
    print("No se puede dividir por cero.")
