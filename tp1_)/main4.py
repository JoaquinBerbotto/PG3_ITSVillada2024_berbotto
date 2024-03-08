def orden(list):
    list_ord = sorted(list, reverse=True)
    return list_ord

def main():
    ent = input("Ingrese sus numeros separados por espacios: ")
    list_orig = [int(x) for x in ent.split()]
    list_ord = orden(list_orig)
    print("Lista ordenada:", list_ord)

main()