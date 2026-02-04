print ('Bem vindo ao contador automatico, vamos começar ')
inicio = input("de onde você quer começar? ")
fim = input("aonde você quer chegar? ")
dquanto = input("de quanto em quanto você vai? ")
inicio, fim, dquanto = int(inicio), int(fim), int(dquanto)
if inicio == fim:
    print ("você ja esta aonde quer estar")
if inicio > fim:
    while inicio > fim - dquanto:
        print (inicio)
        inicio -= dquanto
else:
    while inicio < fim + dquanto :
        print (inicio)
        inicio += dquanto