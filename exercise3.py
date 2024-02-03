first_value = input('Digite o primeiro valor: ')
second_value = input('Digite o segundo valor: ')

if first_value == second_value:
    print(f'{first_value=} é igual a {second_value=}')
elif first_value < second_value:
    print(f'{first_value=} é menor que {second_value=}')
else:
    print(f'{first_value=} é maior que {second_value=}')