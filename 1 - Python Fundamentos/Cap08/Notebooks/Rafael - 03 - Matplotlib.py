import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

periodo = pd.date_range('01/03/2019', periods=15, freq='D')
valorVenda = [round(x, 2) for x in np.random.random_sample(15) * 9.65]
margem = np.random.randint(15, 25, len(valorVenda))

# Junta os 2 objetos
x = np.stack((valorVenda, margem))

labels = ['Valor Venda', 'Margem']

fig, ax = plt.subplots()
ax.stackplot(periodo, valorVenda, margem, labels=labels)
ax.legend(loc='upper left')
plt.show()