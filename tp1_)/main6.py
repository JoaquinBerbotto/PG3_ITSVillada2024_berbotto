def cont_voc(frase):
    voc = "aeiouAEIOU"
    cant_voc = 0
    for car in frase:
        if car in voc:
            cant_voc += 1
    return cant_voc

# Ejemplo de uso:
frase = input("Ingresa una frase: ")
print("La cantidad de vocales en la frase es:", cont_voc(frase))
