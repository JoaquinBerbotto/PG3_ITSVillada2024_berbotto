class mates:
    def __init__(self):
        self.num1 = int(input("Ingrese el primer numero: "))
        self.num2 = int(input("Ingrese el segundo nero: "))
        self.matear()

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "No se puede dividir por cero."

    def matear(self):
        print("Suma:", self.suma())
        print("Resta:", self.resta())
        print("Multiplicación:", self.multiplicacion())
        print("División:", self.division())


mates = mates()
