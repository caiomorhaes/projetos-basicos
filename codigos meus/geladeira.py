print (' Você acabou de abrir a sua geladeira, nela você busca uma bebida, uma comida e uma sobremesa')
bebida = ['coca','guarana','h20','suco natural']
comida = ['macarrao','arroz e ovo','lasanha','hamburguer']
sobremesa = ['sorvete','açai','bolo','fruta']
print('                    ')
resultado1 = 'N'
while resultado1 != 'S':
    print(bebida)
    selecao_bebida = input ('Selecione uma bebida para começar(0-3): ')
    selecao_bebida = int(selecao_bebida)
    print('                    ')
    resultado1 = input ('você selecionou ' + bebida[selecao_bebida] + '? [S,N]  ').upper()
    print('                    ')
    a = bebida[selecao_bebida]
print ('Agora para a comida')
resultado2 = 'N'
while resultado2 != 'S':
    print(comida)
    selecao_comida = input ('Selecione uma comida(0-3) ')
    selecao_comida = int(selecao_comida)
    print ('                    ')
    resultado2 = input ('você selecionou ' + comida[selecao_comida] + '? [S,N]  ').upper()
    print('                    ')
    b = comida[selecao_comida]
print ('Agora para a sobremesa')
resultado3 = 'N'
while resultado3 != 'S':
    print(sobremesa)
    selecao_sobremesa = input ('Selecione uma sobremesa(0-3): ')
    selecao_sobremesa = int(selecao_sobremesa)
    print('                    ')
    resultado3 = input ('você selecionou ' + sobremesa[selecao_sobremesa] + '? [S,N]  ').upper()
    print('                    ')
    c = sobremesa[selecao_sobremesa]
print (f'Parabens, no fim você selecionou {a} para beber, {b} para comer e {c} para sobremesa')

