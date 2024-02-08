name = input('Digite seu nome: ')
age = input('Digite sua idade: ')

if len(name) == 0 or len(age) == 0:
    print('Desculpe, voce deixou campos vazios.')
    exit(0)

int_age = int(age)

print(f'Seu nome é {name}')

print(f'Seu nome invertido é {name[::-1]}')

if name.count(' ') > 0:
    print('Seu nome contém espaços')
else:
    print('Seu nome não contém espaços')

print(f'Seu nome tem {len(name)} letras')

print(f'A primeira letra do seu nome é {name[0]}')

print(f'A última letra do seu nome é {name[-1]}')

