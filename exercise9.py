sales = list()

option = input('Selecione uma opção \n[i]inserir [a]pagar [l]istar [s]air: ')

while option != 's':
    if option == 'i':
        item = input('Digite o item: ')
        if item:
            sales.append(item)
        else:
            print('Item inválido.')
    elif option == 'a':
        index_input = input('Digite o indice do item para apagar: ')
        try:
            index = int(index_input)
            sales.remove(sales[index])
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif option == 'l':
        if len(sales) == 0:
            print('Não há itens.')
        else:
            indexed = enumerate(sales)

            for index, value in indexed:
                print(index, value)
    else:
        print('Opção inválida.')

    option = input('Selecione uma opção \n[i]inserir [a]pagar [l]istar [s]air: ')