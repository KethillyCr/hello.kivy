class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def Andar(self):
        print("Andou")

class Carro:
    def __init__(self):
        self.veiculo = "abrir_porta"

    def Abrir_porta(self):
        print("Porta aberta")

class Moto:
    def __init__(self):
        self.veiculo = "empinar"

    def Empinar(self):
        print("Empinando")

print("")
print("Carro")
carro = Carro()
carro.Abrir_porta()

print("")
print("Moto")
moto = Moto()
moto.Empinar()

print("")
print("Veiculo")
veiculo = Veiculo("Ford","Fiesta")
print(veiculo.marca)
print(veiculo.modelo)