"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

name = input('Digite o primeiro nome: ')

if len(name) > 6:
    print('Seu nome é muito grande')
elif len(name) <= 4:
    print('Seu nome é curto')
else:
    print('Seu nome é normal')