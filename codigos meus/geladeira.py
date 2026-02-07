#introdução
print (' Você acabou de abrir a sua geladeira, nela você busca uma bebida, uma comida e uma sobremesa')
#listas
bebida = ['coca','guarana','h20','suco natural']
comida = ['macarrao','arroz e ovo','lasanha','hamburguer']
sobremesa = ['sorvete','açai','bolo','fruta']
print('                    ')
#estabelecer uma logica para o while
resultado1 = 'N'
while resultado1 != 'S':
    #evitar que o usuario coloque letras no input
    while True:
        print(bebida)
        selecao_bebida = (input ('Selecione uma bebida para começar(0-3): '))
        if not (selecao_bebida.isdigit()):
            print('                    ')
            print("-" * 30)
            print('por favor só insira números no terminal')
            print("-" * 30)
            print('                    ')
            continue
        selecao_bebida = int(selecao_bebida)
        if not selecao_bebida <= 3 and selecao_bebida >= 0:
            print('                    ')
            print("-" * 30)
            print('não insira números alem ou abaixo da quantidade de números na lista ')
            print("-" * 30)
            print('                    ')
            continue
        break
    #formatar para int para ler na lista
    print('                    ')
    #enfase no .upper para evitar que o usuario coloque a resposta em minusculo
    resultado1 = input ('você selecionou ' + bebida[selecao_bebida] + '? [S,N]  ').upper()
    print('                    ')
    a = bebida[selecao_bebida]
print ('Agora para a comida')
resultado2 = 'N'
while resultado2 != 'S':
    while True:
        print(comida)
        selecao_comida = input ('Selecione uma comida(0-3) ')
        if not (selecao_comida.isdigit()):
            print('                    ')
            print("-" * 30)
            print('por favor só insira numeros no terminal')
            print("-" * 30)
            print('                    ')
            continue
        selecao_comida = int(selecao_comida)
        if not selecao_comida <= 3 and selecao_comida >= 0:
            print('                    ')
            print("-" * 30)
            print('não insira números alem ou abaixo da quantidade de números na lista ')
            print("-" * 30)
            print('                    ')
            continue
        break
    print ('                    ')
    resultado2 = input ('você selecionou ' + comida[selecao_comida] + '? [S,N]  ').upper()
    print('                    ')
    b = comida[selecao_comida]
print ('Agora para a sobremesa')
resultado3 = 'N'
while resultado3 != 'S':
    while True:
        print(sobremesa)
        selecao_sobremesa = input ('Selecione uma sobremesa(0-3): ')
        if not (selecao_sobremesa.isdigit()):
            print('                    ')
            print("-" * 30)
            print('por favor só insira numeros no terminal')
            print("-" * 30)
            print('                    ')
            continue
        selecao_sobremesa = int(selecao_sobremesa)
        if not selecao_sobremesa <= 3 and selecao_sobremesa >= 0:
            print('                    ')
            print("-" * 30)
            print('não insira números alem ou abaixo da quantidade de números na lista ')
            print("-" * 30)
            print('                    ')
            continue
        break
    print('                    ')
    resultado3 = input ('você selecionou ' + sobremesa[selecao_sobremesa] + '? [S,N]  ').upper()
    print('                    ')
    c = sobremesa[selecao_sobremesa]
print (f'Parabens, no fim você selecionou {a} para beber, {b} para comer e {c} para sobremesa')


