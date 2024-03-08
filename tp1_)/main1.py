def buscar_elemento(liston, e):
    try:
        indice = liston.index(e)
        return indice
    except ValueError:
        return "El elemento no se encuentra en la lista"

lista = [1, 3, 5, 7, 9, 11, 13]

e_buscado = int(input("Ingrese el elemento que desea buscar: "))

result = buscar_elemento(lista, e_buscado)

print("Indice:", result)