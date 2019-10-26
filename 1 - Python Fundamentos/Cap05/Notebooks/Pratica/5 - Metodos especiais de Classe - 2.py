class Livro():
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        print('Construtor invocado')

    # Metodo __str__ permite utilizar o print no objeto
    def __str__(self):
        return f'Titulo: {self.titulo}. Autor: {self.autor}. Ano: {self.ano}'

    # Metodo __len__ permite utilizar um len(objeto)
    def __len__(self):
        return self.ano

    # Metodo criado dessa forma permite utilizar o objeto.len()
    def len(self):
        return f'A quantidade do ano é {self.ano}'


# Instanciamos a classe em um objeto
livr = Livro('Meg a mocinha manhosa', 'Meg Ferreira', 2018)


# Como existe o metodo especial __str__ na classe podemos dar um print no objeto
print(livr)


# Como existe o metodo __len__ podemos chamar o len(objeto)
print(len(livr))

# Ja para chamar o metodo len(self) é necessario fazer da seguinte forma
print(livr.len())