# if / elif      / else
# se / se não se / se não
prompt = input('Você quer "entrar" ou "sair"? ')

if prompt == 'entrar':
    print('Você entrou no sistema')

    print(12341234)
elif prompt == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')