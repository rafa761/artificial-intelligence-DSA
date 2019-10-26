'''A funcao filter aplica um filtro a uma lista
é passado uma funcao booleana (True ou False)
Caso o resultado seja True a funcao filter retorna o valor
Caso seja False elimina o item do resultado

Assim como o map, o filter retorna um objeto do tipo iterator, sendo necessario
converter para lista'''

def verificaPar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# print(verificaPar(6))

listaNum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

pares = list(filter(verificaPar, listaNum)) # Filter precisa ser convertido para lista
print(f'Os numeros pares sao: {pares}')

# filter também pode ser utilizado com lambda
par = list(filter(lambda val: val % 2 == 0, listaNum))
print(f'Pares com lambda: {par}')

# Filtrando somente numeros maiores que determinado valor
print(list(filter(lambda val: val > 8, listaNum)))