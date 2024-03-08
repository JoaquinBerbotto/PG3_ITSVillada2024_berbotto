def dib_rect(ancho, alto, car):
    for i in range(alto):
        for j in range(ancho):
            print(car, end="")
        print()

def dib_tria(base, car):
    for i in range(1, base + 1):
        print(car * i)

def main():
    print("1. Dibujar rectangulo")
    print("2. Dibujar triangulo")
    op = int(input("¿Qué queres dibujar?"))

    if op == 1:
        ancho = int(input("Introduce el ancho del rectangulo: "))
        alto = int(input("Introduce el alto del rectangulo: "))
        car = input("Introduce el caracter a utilizar: ")
        dib_rect(ancho, alto, car)
    elif op == 2:
        base = int(input("Introduce la base del triangulo: "))
        car = input("Introduce el caracter a utilizar: ")
        dib_tria(base, car)
    else:
        print("Opcion no valida.")

main()
