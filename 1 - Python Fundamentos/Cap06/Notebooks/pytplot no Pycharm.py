import sqlite3
import matplotlib.pyplot as plt

# Esta´sendo usado o banco 'base_teste2.db' criado em outro exercicio
banco = "base_teste2.db"


def monta_grafico():
    lst_id = []
    lst_valor = []
    cursor.execute("select id, valor from produtos")
    dados = cursor.fetchall()

    for linha in dados:
        lst_id.append(linha[0])
        lst_valor.append(linha[1])

    # Barras Verticais
    plt.bar(lst_id, lst_valor)
    plt.show()

    #Barras horizontais
    # plt.barh(lst_id, lst_valor)
    # plt.show()

    # Grafico linha
    # plt.semilogx(lst_id, lst_valor)
    # plt.show()


if __name__ == "__main__":
    with sqlite3.Connection(banco) as conexao:
        cursor = conexao.cursor()

        monta_grafico()
