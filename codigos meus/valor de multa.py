print('Olá Bem vindo ao site da biblioteca, vamos acertar suas pendências? estou vendo que possui livros entregues que tiveram atraso, vamos continuar')
print()
#evitar de letras serem colocadas no codigo de forma incorreta pelo usuario, evitando missinputs
while True:
    dias_atraso = (input('A quantos dias vai fazer o atraso? '))
    if not (dias_atraso.isdigit()):
        print("-" * 30)
        print ('por favor só insira numeros no terminal')
        print("-" * 30)
        continue
    break
#formatar o input que sempre sai str para int para os futuros calculos
dias_atraso = int(dias_atraso)
print()
if dias_atraso < 3:
    print ('Desta vez sairá sem pagar nada, mas fique atento')
elif (dias_atraso >= 3) and (dias_atraso < 4 ):
    preco = dias_atraso * 0.50
    print (f'Por causa de seu atraso, terá que pagar 50 centavos por dia, no seu caso sendo {preco}R$')
elif (dias_atraso >= 4) and (dias_atraso <7) :
    preco = dias_atraso * 1
    print (f'Por causa de seu atraso, terá que pagar 1 real por dia, no seu caso sendo {preco}R$')
else:
    preco = dias_atraso * 2
    print (f'Por causa de seu atraso, terá que pagar 2 reais por dia, no seu caso sendo {preco}R$')
