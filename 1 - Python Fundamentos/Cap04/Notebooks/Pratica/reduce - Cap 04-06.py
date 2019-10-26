# reduce foi movido para o modulo functools, sendo necessario importar
from functools import reduce

def soma(val1, val2):
    total = val1 + val2
    return total

lista = [60, 5, 34, 46, 8, 2]

'''Reduce recebe uma funcao e uma lista
ele aplica a funcao ao primeiro elemento da lista
o resultado é aplicado ao segundo elemento
entao pega esse novo resultado e aplica ao terceiro
assim sucessivamente até que chegar ao final da lista'''

print(reduce(soma, lista))

# reduce também pode ser utilizado com lambda
print(reduce(lambda val1, val2: val1 + val2, lista))

# pode ser utilizado para encontrar o maior valor em uma lista
resultMaior = reduce(lambda val1, val2: val1 if val1 > val2 else val2, lista)
print(f'O Maior numero da lista é {resultMaior}')

