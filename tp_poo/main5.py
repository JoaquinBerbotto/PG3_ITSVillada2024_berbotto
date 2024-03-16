class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))
        print("Sueldo:", self.sueldo)

    def impuesto(self):
        if self.sueldo > 3000:
            print(f"El empleado debe pagar impuestos.\n")
        else:
            print("El empleado no debe pagar impuestos.")


persona = Persona()



empleado = Empleado()


empleado.impuesto()
