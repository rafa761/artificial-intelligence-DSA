# Value Error
'''try:
    numero = int(input('Informe um numero: '))
except ValueError:
    print('Numero invalido')
'''

# Type Error
try:
    result = 8 + 'r'
except TypeError:
    print('Tipos de dados invalidos para Soma')

# Io Error
try:
    arquivo = open('/home/rafael/PycharmProjects/Cursos_e_Aprendizado/Curso I.A. Data Science Academy/1 - Python Fundamentos/Cap04/Notebooks/arquivos/testandoerros.txt', 'w')
    arquivo.write('Gravando arquivo')
except IoError:
    print('Arquivo nao encontrado ou nao pode ser salvo')
else:
    print('Arquivo gravado com sucesso')
    arquivo.close()


try:
    arquivo = open('arquivoQueNaoExiste', 'r')
except IOError:
    print('O arquivo nao existe')


# Dessa forma ocorre o erro da linguagem Python
def pedeInt():
    valor = int(input('Digite um numero inteiro: '))
    print(f'O Valor digitado foi: {valor}')
#pedeInt()

# Dessa forma esta tratado
def pedeIntTrat():
    try:
        valor = int(input('Digite um numero inteiro: '))
    except ValueError:
        print('VOce nao digitou um numero')
    else:
        print(f'O numero digitado foi: {valor}')

# pedeIntTrat()

# Pede para o usuario redigitar caso nao seja inteiro, porem caso seja feita uma segunda tentativa ocorre erro
def pedeMultiInt():
    try:
        valor = int(input('Digite um numero inteiro: '))
    except ValueError:
        print('Voce nao digitou um numero, tente novamente')
        valor = int(input('Digite um numero inteiro: '))
    finally:
        print(f'Numero digitado: {valor}. Obrigado')

# pedeMultiInt()

print()
# Dessa forma é feito um while para tratar enquanto nao for digitado o numero correto
def pedeMultiIntTratado():
    while True:
        try:
            valor = int(input('Digite um Numero inteiro: '))
        except ValueError:
            print('Nao foi digitado um numero, tente novamente')
            continue
        else:
            print(f'FOi digitado: {valor}')
            break
        finally:
            print('Fim da execucao. Obrigado')

# pedeMultiIntTratado()


# Tambem podem ser feitos tratamentos para operacoes nao permitidas
tupla = (1, 2, 3, 4, 5)
print(tupla)

try:
    tupla.append(6) # Tupla nao tem o metodo append, causando erro
except AttributeError as NomeErro: # Pode ser armazenado o erro em variavel
    print(f'Tuplas nao tem o metodo apend. Erro: {NomeErro}')


print()
try:
    arquivo = open('arquivoQueNaoExiste', 'r')
except IOError as NomeErro:
    print(f'Erro: {NomeErro}')


# Erro de importacao de modulo
try:
    import moduloDoidao
except ImportError as ErroImportacao:
    print(f'Importacao de Modulo invalida. {ErroImportacao}')


# Erro referenciando chave inexistente em dicionario
dicionario = {'chave':6}
try:
    print(dicionario['chaveNaoExistente'])
except KeyError as ErroChave:
    print(f'A Chave nao foi encontrada no dicionario. {ErroChave}')


# Unbound Local Error é quando é tentado referenciar uma variavel que nao teve nada atribuido
try:
    print(variavelInexistente)
except NameError as ErroNaoIniciado:
    print(ErroNaoIniciado)


# o comando raise serve para chamar/mostrar um erro
# raise ValueError

# Tambem pode ser adicionada uma mensagem ao comando raise para ser exibida no erro
print('Teste Raise')
# raise NameError('Variavel nao foi definida')


# raise pode ser utilizado para mostrar qualquer tipo de erro que tenha ocorrido
try:
    print(5 / 0)
except:
    print('Nao foi possivel fazer a divisao')
    raise