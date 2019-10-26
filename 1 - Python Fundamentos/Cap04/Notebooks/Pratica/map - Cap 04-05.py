'''A Funcao MAP aplica uma funcao a uma lista
Passando uma funcao no primeiro parametro, a mesma é executada para cada item
na lista que é passada no segundo parametro'''

def fahrenheit(temp): # Funcao que converte uma temperatura em fahrenheit
    return ((float(9) / 5) * temp + 32)


def celsius(temp): # Funcao que converte uma temperatura em Celsius
    return (float(5) / 9) * (temp - 32)

# print(celsius(200))
# print(fahrenheit(50))

# Lista de temperaturas
temperaturas = [15, 40, 100, 64, 2]


lstConvertida = map(fahrenheit, temperaturas) # Map aplica a funcao a cada item da lista
print(list(lstConvertida))
print(list(map(celsius, temperaturas))) # No Python 3 é necessario converter o resultado do MAP para Lista

for T in list(map(fahrenheit, temperaturas)): # Resultado do MAP pode ser iterado
    print(T)
print()

lstConvertlbda = list(map(lambda T:(float(9) / 5) * T + 32, temperaturas)) # Pode ser usada lambda dentro do Map
print(f'Lista com lambda e map: {lstConvertlbda}')


lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

# Pode ser passado Lambda com mais de um parametro para a funcao MAP
listaSomada = list(map(lambda val1, val2: val1 + val2, lista1, lista2))
print(f'Somando 2 Lista com Lambda: {listaSomada}')

# usando map e lambda com 3 listas

listaA = [1, 2, 3, 4]
listaB = [5, 6, 7, 8]
listaC = [9, 10, 11, 12]

listaSoma3 = list(map(lambda val1, val2, val3: val1 + val2 + val3, listaA, listaB, listaC ))
print(f'Somando 3 listas com lambda e MAP: {listaSoma3}')
