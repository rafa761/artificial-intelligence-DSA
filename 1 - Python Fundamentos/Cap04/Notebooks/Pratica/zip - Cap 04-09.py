'''Zip é utilizado para unir 2 listas de elementos
O Resultado do Zip é um objeto do tipo iterator
Transformando ele em uma lista com o list() temos uma lista de tuplas'''

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7]
listaResult = list(zip(lista1, lista2))
print(f'As 2 listas unidas é {listaResult}')

# Tambem pode ser utilizado para unir listas de String
listaS1 = ['ABCDE']
listaS2 = ['xyz']
listaSResult = list(zip(listaS1, listaS2))
print(f'As strings unidas são: {listaSResult}')

# Zip Tambem pode ser utilizo para inverter um dicionario
dicionario1 = {'nome':'Meg', 'idade':3}
dicionario2 = {'apelido':'manhosa', 'patinhas':4}
print(f'Dict 1: {dicionario1}')
print(f'DIct 2: {dicionario2}')

# Dessa forma serao unidos apenas as chaves dos dicionarios
result = list(zip(dicionario1, dicionario2))
print(f'Com chaves unidas pelo zip: {result}')

# Dessa forma as chaves do primeiro serao unidos aos valores do segundo
result2 = list(zip(dicionario1, dicionario2.values()))
print(f'Chave de uma lista com valor da outra: {result2}')


# A funcao abaixo retorna o mesmo resultado que o zip acima: Troca um valor de dicionario
def trocaDict(dicio1, dicio2):
    dicioTemp = {}
    for dicio1key, dicio2value in zip(dicio1, dicio2.values()):
        dicioTemp.update({dicio1key:dicio2value})
    return dicioTemp

print(trocaDict(dicionario1, dicionario2))