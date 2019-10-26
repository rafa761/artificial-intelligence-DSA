class Cachorro():
    def __init__(self, raca, nome):
        self.raca = raca
        self.nome = nome
        print('O construtor foi invocado para criar o objeto')

    def latir(self):
        print(f'O cachorro {self.nome} latiu. AU AU')


meg = Cachorro('Vira Lata', 'Meg') # criando um objeto Instanciando a classe
meg.latir() # chamando um metodo do objeto

# Perguntando ao objeto se ele possui um atributo
print(hasattr(meg, "nome"))
print(hasattr(meg, "raca"))
print(hasattr(meg, "atributo inexistente")) # Retorna False porque o objeto nao tem esse atributo

# Altera um atributo do objeto
setattr(meg, "raca", "dogao")
print(meg.raca) # Atributo foi alterado

# Podemos deletar atributos dos objetos
delattr(meg, "nome")
print(meg.nome) # Atributo nao existe mais


# Podemos buscar quais sao os atributos do objeto
print(getattr(meg, "raca"))
