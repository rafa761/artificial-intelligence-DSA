import sqlite3
import os

# Captura diretorio de trabalho
diretorio_trabalho = os.getcwd()

# Define nome do banco
banco = diretorio_trabalho + "\\" + "banco_teste.db"
print("Definindo banco de dados como: ", banco)

# Remove o Banco e Recria
os.remove(banco) if os.path.exists(banco) else None
print("Removendo banco de dados antigo")

# Abre Conexao com o arquivo de banco
# Usando with o arquivo é automaticamente fechado ao final do uso
with sqlite3.Connection(banco) as conexao:
    print("Abrindo Conexao com Banco: ", type(conexao))

    # Define um Cursor
    cursor = conexao.cursor()
    print("Abrindo Cursor: ", type(cursor))

    # SQL para criar tabela
    # Clausura "if no exists" só cria a tabela caso ela NAO exista
    sql_create = """create table if not exists tabela_exemplo(
                        id integer primary key,
                        nome varchar(100),
                    sobrenome varchar(120)
                    )"""
    print("SQL de create tabel definido")

    # Executa o comando
    cursor.execute(sql_create)
    print("SQL de Create table executado")

    # Modelo de SQL usado para fazer insert
    sql_insert = "insert into tabela_exemplo values (?, ? ,? )"
    print("Modelo de SQL de Insert Definido")

    # DataSet de Dados que serao inseridos
    dataset_dados = [(82, "Rafael", "Ferreira"),
                     (84, "Maffu", "Ferreira"),
                     (98, "Meg", "Lindona")]
    print("Dataset de dados definido: ", dataset_dados)

    # Executa o comando de insert passando o DataSet como Parametro
    for registro in dataset_dados:
        cursor.execute(sql_insert, registro)
    conexao.commit()
    print("Comando de Insert executado, transacao Comitada")

    # Define Comando de Select
    sql_select = "select * from tabela_exemplo"
    print("SQL de select definido: ", sql_select)

    # Exibe os dados existentes
    print("Dados da tabela: \n")
    cursor.execute(sql_select)
    dados = cursor.fetchall()

    for dado in dados:
        print(dado)
