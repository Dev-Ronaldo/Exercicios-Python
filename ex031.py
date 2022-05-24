#Exercicio 031 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas

distancia=float(input('Digite a distância da viagem:'))

if distancia<=200:
    valor=distancia*0.50
    print('A distância é {}Km e o valor da viagem é R${:.2f}'.format(distancia, valor))
else:
    valor=distancia*0.45
    print('A distância é {}Km e o valor da viagem é R${:.2f}'.format(distancia, valor))
