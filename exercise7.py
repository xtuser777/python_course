secret_word = input('Digite a palavra secreta: ')

count = 0

right = ''

predict_word = input('Digite uma letra adivinhando, ou digite 0 para sair: ')

result = ''
while predict_word != '0':
    count += 1
    
    if predict_word in secret_word:
        result = ''
        right += predict_word
        for letter in secret_word: 
            attach = False
            for ltr in right:   
                if letter == ltr:
                    attach = True
                    result += ltr
            if not attach:
                result += '*'

    if result == secret_word:
        print('Você adivinhou a palavra.')
        break
    else:    
        print(result)
        predict_word = input('Digite uma letra adivinhando, ou digite 0 para sair: ')

print(f'Contagem de tentativas: {count}')
