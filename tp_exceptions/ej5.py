try:
    with open("archivo.txt", "w") as archivo:
        serie_strings = ["Hola", "amigazo,""esto", "es", "una", "serie", "de", "strings", 21]
        for string in serie_strings:
            archivo.write(string + "\n")
except TypeError:
    print("Escribiste un tipo de dato incorrecto.")
