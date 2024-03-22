class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imp_info(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def mensaje(self):
        if self.nota >= 6:
            print("El alumno", self.nombre, "esta regular.")
        else:
            print("El alumno", self.nombre, "no esta regular.")


alumno1 = Alumno("Pedro", 7)
alumno2 = Alumno("Ana", 5)

alumno1.imp_info()
alumno2.imp_info()

alumno1.mensaje()
alumno2.mensaje()
