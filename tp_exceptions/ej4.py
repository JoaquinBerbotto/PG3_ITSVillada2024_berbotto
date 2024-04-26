try:
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo: "))
    resu = num1 / num2
    print("Tu calculo da:", resu)
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except ValueError:
    print("Tenes que ingresar numeros validos.")
