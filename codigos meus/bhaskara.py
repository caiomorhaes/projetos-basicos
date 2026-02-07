#tentar fazer uma calculadora de bhaskara interativa
#introdução

print("Olá bem vindo a CALCULADORA DE BHASKARA AUTOMATICA")
print("A seguir vou pedir o numero de suas 3 variaveis")
import math 
#while true para evitar do uso de letras
while True:
#variaveis da equação
    A = input("Entre com o valor de A: ")
    print    ("                        ")
    B = input("Entre com o valor de B: ")
    print    ("                        ")
    C = input("Entre com o valor de C: ")
    print    ("                        ")
    if not (A.isdigit() and B.isdigit() and C.isdigit()):
        print ('Por favor, insira só números, sejam eles decimais ou inteiros')
        continue
    break
#formatando as variaveis para floats
A,B,C = map(int,(A,B,C))
#calculo de delta
delta = (B*B - (4 * A * C))
print ('Este é o valor do seu DELTA:',delta)
#delta negativo não tem raiz
if delta < 0:
    print("                        ")
    print('NÃO exite valor de raizes para esse valor de delta :(')
#delta = a 0 só tem uma raiz, os dois calculos dao no mesmo
if delta == 0:
    print("                        ")
    # calculo das raizes
    raiz2 = float((-B - math.sqrt(delta)) / (2 * A))
    print(f'Para esse valor de delta só existe UMA raiz, nesse caso sendo:  {raiz2:.2f} ')
#delta maior que 0 é o padrao com duas raizes
if delta > 0:
    print("                        ")
    # calculo das raizes
    raiz1 = float((-B + math.sqrt(delta)) / (2 * A))
    raiz2 = float((-B - math.sqrt(delta)) / (2 * A))
    print (f'Essas são as DUAS raizes reais desta operação: {raiz1:.2f}, {raiz2:.2f} ')
print('FIM DO SISTEMA')

