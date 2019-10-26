'''List comprehension permite aplicar uma funcao arbitraria a uma
sequencia de elementos.
essa tecnica é levemente mais rapida do que o MAP'''

lista1 = [x for x in range(1,11)]
print(lista1)

# Pode ser utilizado para separar uma cadeia de caracteres
lista2 = [x for x in 'Python']
print(lista2)

# Pode ser utilizado para aplicar qualquer calculo matematico a uma cadeia de elementos ou lista
celsius = [10, 29, 50, 65, 100]
fahrenheit = [((float(9) / 5) * temp + 32) for temp in celsius]
print(f'Temperaturas: {fahrenheit}')


# Pode ser utilizado list comprehension aninhado, ou seja: Um list comprehension dentro de outro
lista3 = [x ** 2 for x in [y ** 2 for y in range(1,11)]]
print(f'Numeros elevados ao quadrado 2x {lista3}')
