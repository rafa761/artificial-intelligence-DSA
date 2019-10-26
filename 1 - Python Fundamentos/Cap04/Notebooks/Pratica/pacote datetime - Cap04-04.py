import datetime

# Data
print(datetime.date.today()) # Pega a data atual
hoje = datetime.date.today() # Armazena a data atual em uma variavel, que fica com tipo date
print(datetime.date.ctime(hoje)) # ctime recebe objeto do tipo date
# objeto do tipo date possui as funcoes abaixo
print(f'''
Ano: {hoje.year}
mes: {hoje.month}
dia: {hoje.day}
''')



# Data e Hora
print(datetime.datetime.today()) # Pega a data e Hora atual
dataHora = datetime.datetime.today() # Armazena a data e hora em uma variavel, que fica com tipo datetime
print(datetime.datetime.ctime(dataHora)) # ctime recebe objeto do tipo datetime
print(datetime.datetime.date(dataHora)) # Pega somente a data de uma variavel datetime
print(datetime.datetime.time(dataHora)) # Pega somente a hora de uma variavel datetime
# Objeto do tipo datetime possui funcoes de data e hora
print(f'''
Horas: {dataHora.hour}
Minutos: {dataHora.minute}
segundos: {dataHora.second}

Ano: {dataHora.year}
Mes: {dataHora.month}
Dia: {dataHora.day}
''')