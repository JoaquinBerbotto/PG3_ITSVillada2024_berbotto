class Persona:
    def __init__(self):
        self.nomb = ""

    def inici_nombre(self, nomb):
        self.nomb = nomb

    def mostrar_nombre(self):
        print("Nombre:", self.nomb)

persona1 = Persona()
persona2 = Persona()

# Inicializar los nombres de las personas
persona1.inici_nombre("Juan")
persona2.inici_nombre("María")

# Mostrar los nombres de las personas
persona1.mostrar_nombre()
persona2.mostrar_nombre()
