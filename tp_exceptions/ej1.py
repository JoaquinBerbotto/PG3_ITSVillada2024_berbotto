def sumar():
    conti = True
    while conti:
        try:
            a = int(input("Ingresa el primer numero: "))
            b = int(input("Ingresa el segundo numero: "))
            suma = a + b
            print("La suma da:", suma)
        except ValueError:
            print("Tenes que ingresar numeros enteros. PERO NO CEROS")
        finally:
            rta = input("¿Queres seguir sumando? (s/n): ")
            if rta.lower() != 's':
                conti = False

if __name__ == "__main__":
    sumar()
