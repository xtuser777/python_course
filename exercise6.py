name = 'Lucas Oliveira'

new_string = ''

count = 0

while count < len(name):
    new_string += f'*{name[count]}'
    count += 1

print(new_string)