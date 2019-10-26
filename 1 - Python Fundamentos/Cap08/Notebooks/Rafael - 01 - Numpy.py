import numpy as np

array1 = np.array([1, 2, 3, 4])
array2 = np.array([4, 5, 6, 7])
matriz1 = np.array([array1, array2], dtype=np.complex)

print('Array 1', type(array1), array1)
print('Array 2', array2.shape, array2)
print()
print('Matriz1', matriz1)
print(matriz1.dtype)
print(matriz1.shape)
print(matriz1.size)
print(matriz1.itemsize)

lista1 = [1, 8, 16, 20]
matriz2 = np.ndarray(shape=(2, 2), dtype=np.float64)
print(matriz2)
print(matriz2.ndim)

matriz3 = np.array(np.arange(0, 10, 0.5))
print(matriz3)

matriz4 = np.zeros(shape=(3, 3))
print(matriz4)

matriz5 = np.eye(4)
print(matriz5)

matriz6 = np.diag(np.arange(0, 5, 0.5))
print(matriz6)

matriz7 = np.linspace(0, 10)
print(matriz7)

matriz8 = np.logspace(0, 10)
print(matriz8)

matriz9 = np.ones(5)
print(matriz9)

matriz10 = np.random.rand(5)
print(matriz10)

matriz11 = np.random.randint(0, 1000, 5)
print(matriz11)

matriz12 = np.random.random_sample(50)
print(matriz12)

import matplotlib.pyplot as plt

dados = np.random.rand(10)
# plt.show((plt.hist(dados)))

imagem = np.random.randn(30, 30)
plt.imshow(imagem, cmap=plt.cm.hot)
plt.colorbar()