class Triangulo:
    def __init__(self):
        self.l1 = float(input("Ingrese la longitud del primer lado del triangulo: "))
        self.l2 = float(input("Ingrese la longitud del segundo lado del triangulo: "))
        self.l3 = float(input("Ingrese la longitud del tercer lado del triangulo: "))
        self.inic_atr()

    def inic_atr(self):
        self.lados = [self.l1, self.l2, self.l3]
        self.lados.sort(reverse=True)

    def imp_lado_M(self):
        print("El lado mayor del triangulo es:", self.lados[0])

    def equi(self):
        if self.l1 == self.l2 == self.l3:
            print("El triángulo es equilatero.")
        else:
            print("El triángulo no es equilatero.")


triangulo = Triangulo()

triangulo.imp_lado_M()

triangulo.equi()
