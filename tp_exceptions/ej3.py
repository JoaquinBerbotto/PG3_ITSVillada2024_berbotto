try:
    mes = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    num_mes = int(input("Ingrese el número de mes (1-12): "))
    nomb_mes = mes[num_mes - 1]
    print("El mes que le corresponde al ", num_mes, "es:", nomb_mes)
except IndexError:
    print("El numero de mes que pusiste está fuera de rango.")
except ValueError:
    print("Debe ingresar un numero valido.")
