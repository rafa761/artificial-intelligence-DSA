"""Para Criar Classe basta utilizar a palavra reservada class NomeDaClasse():
Por convenção nomes de classe devem sempre iniciar com letra Maiúscula"""

class Livro():
    def __init__(self):
        self.titulo = 'As traquinagens da Maffu'
        self.codigo = 55
        print('O Construtor foi invocado para criar esta classe')

    def imprime(self):
        print(f'Foi criado o livro {self.titulo} com o codigo: {self.codigo}')


# Aqui instanciamos a Classe, ou seja, criamos um objeto do tipo da Classe
objetoLivro = Livro()

# O Objeto pode chamar os métodos da Classe
objetoLivro.imprime()

# Pode ser observado que o objeto é do tipo Livro, que é a classe
print(type(objetoLivro))


print()
# Também podem ser passados parametros na criacao da Classe
class Livro2():
    def __init__(self, titulo, cod):
        self.titulo = titulo
        self.cod = cod
        print('Construtor invocado para criar a Classe')

    def imprime(self):
        print(f'Foi criado o livro {self.titulo} com codigo {self.cod}')


# Criamos um objeto instanciando a Classe, desta vez passando os parametros necessarios no metodo construtor
objetoLivro2 = Livro2('Meg - a Menina Nervosa', 60)

objetoLivro2.imprime()



class Cachorro():
    def __init__(self, raca):
        self.raca = raca

# Criamos um objeto instanciando a classe
meg = Cachorro('Vira Lata')
print(meg.raca) # Podemos verificar o atributo
