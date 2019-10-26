# Criando a Classe
class Circulo():

    # Atributos fora do metodo construtor sao constantes
    pi = 3.14

    def __init__(self, raio = 5):
        self.raio = raio
        print('Metodo Construtor invocado')


    def calcArea(self):
        return (self.raio * self.raio) * Circulo.pi


    def setRaio(self, novoRaio):
        self.raio = novoRaio


    def getRaio(self):
        return self.raio

# Criamos um objeto instanciando a Classe
circ = Circulo() # Criando sem passar parametros é assumido o default do metodo construtor

print(f'O Raio é: {circ.getRaio()}')

print(f'A area é {circ.calcArea()}')