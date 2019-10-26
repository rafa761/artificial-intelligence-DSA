# Criando a Super-Classe
class Animal():
    def __init__(self):
        print('Classe Animal criada')

    def identif(self):
        print('Animal')

    def comer(self):
        print('Comendo')


# Criando a Sub-Classe
class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Classe Cachorro criado')

    def identif(self):
        print('Cachorro')

    def latir(self):
        print('AU AU')



# Instanciamos a Sub Classe em um objeto
maffu = Cachorro()

# Podemos chamar o metodo da Subclasse
maffu.latir()

# Podemos chamar metodos da Super Classe
maffu.comer()

# Caso exista um metodo de mesmo nome entre a Sub Classe e a Super Classe, o Python usará a da SubClasse
maffu.identif()