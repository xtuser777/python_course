"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

str_hour = input('Digite uma hora: ')

try:
    int_hour = int(str_hour)

    if int_hour in range(0, 12):
        print('Bom dia')
    elif int_hour in range(12, 18):
        print('Boa tarde')
    elif int_hour in range(18, 24):
        print('Boa noite')
    else:
        print('Hora incorreta.')
except:
    print('Hora em formato incorreto.')