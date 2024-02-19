"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
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

final_result = result * 10

digit1 = final_result % 11 if final_result % 11 < 9 else 0

result_digit1 = digit1 == int(cpf[-2])

print (result_digit1)
