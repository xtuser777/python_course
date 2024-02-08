"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

str_number = input('Digite um número inteiro: ')

try:
    int_number = int(str_number)

    if int_number % 2 == 0:
        print('O número digitado é par.')
    else:
        print('O número digitado é ímpar.')
except:
    print('Este não é um número inteiro')