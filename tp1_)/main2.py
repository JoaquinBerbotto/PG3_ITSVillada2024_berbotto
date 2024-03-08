def bis(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

def main():
    anio = int(input("Introduce un anio: "))
    if bis(anio):
        print(f"{anio} es bisiesto.")
    else:
        print(f"{anio} no es bisiesto.")

main()