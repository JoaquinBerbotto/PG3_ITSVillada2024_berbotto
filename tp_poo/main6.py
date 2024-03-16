class Familia:
    def __init__(self, n_padre, n_mama, hijos):
        self.n_papa = n_padre
        self.n_mama = n_mama
        self.hijos = hijos

    def __str__(self):
        hijos_str = ", ".join(self.hijos)
        return f"Papa: {self.n_papa}, Mama: {self.n_mama}, Hijos: {hijos_str}"


if __name__ == "__main__":
    n_papa = "Javier"
    n_mama = "Fatima"
    hijos = ["Murray", "Lucas", "Milton", "Robert"]

    familia = Familia(n_papa, n_mama, hijos)
    print(familia)
