class Animal:
    def __init__(self, name):
        self.name = name

    def fazer_som(self):
        print("O animal está fazendo um som")


class Cachorro(Animal):
    def __init__(self, name, raça):
        super().__init__(name)
        self.raça = raça

    def fazer_som(self):
        print("O cachorro faz au au")