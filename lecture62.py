"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
formated_cpf = '746.824.890-70'

cpf = formated_cpf.replace('.', '').replace('-', '')

count = 10
index = 0

result = 0

while count >= 2:
    result += count * int(cpf[index])
    count -= 1
    index += 1

final_result1 = result * 10

digit1 = final_result1 % 11 if final_result1 % 11 < 9 else 0

result_digit1 = digit1 == int(cpf[-2])

result += count * int(cpf[index])

final_result2 = result * 10

digit2 = final_result2 % 11 if final_result2 % 11 < 9 else 0

result_digit2 = digit2 == int(cpf[-1])

if (result_digit1 and result_digit2):
    patterns = [
        '0'*11,
        '1'*11,
        '2'*1,
        '3'*11,
        '4'*11,
        '5'*11,
        '6'*11,
        '7'*11,
        '8'*11,
        '9'*11,
    ]
    if cpf in patterns:
        print('CPF inválido')
    else:
        print('CPF válido')
else:
    print('CPF inválido')
