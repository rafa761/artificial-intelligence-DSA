'''Enumerate retorna o indice em uma sequencia de caracteres a medida que itera ele
o Enumerate tem um resultado do tipo iterator, que precisa ser convertido para uma lista
list()
'''

sequencia = ['A', 'B', 'C']
resultado = enumerate(sequencia)
print(list(resultado))

# Pode ser iterado com loop for
for indice, valor in enumerate(sequencia):
    print(f'Indice {indice}. Valor {valor}')
print()

# Tambem pode ser utilizado para manipular e aplicar filtros em uma lista de itens
sequencia2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice, valor in enumerate(sequencia2):
    if indice > 3:
        break
    else:
        print(f'indice {indice}. Valor {valor}')

print()
# Retorna o indice mesmo em lista de Strings
sequencia3 = ['Meg', 'Maffu', 'Andressa']
for indice, valor in enumerate(sequencia3):
    print(f'ind: {indice}. val: {valor}')


# Como uma string é uma cadeira de caracteres, o enumerate pode retornar o indice das letras
sequencia4 = 'A Maffu é fofinha'
for indice, valor in enumerate(sequencia4):
    print(indice, valor)