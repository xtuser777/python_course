"""
Basic strings formatation
s - string
d - int
f - float
.<number of digits>f
x ou X - Hexadecimal
(character)(><^)(quantity)
> - Left
< - Right
^ - Center
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variable = 'ABC'
print(f'{variable}')
print(f'{variable: >10}')
print(f'{variable: <10}.')
print(f'{variable: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variable!r}')