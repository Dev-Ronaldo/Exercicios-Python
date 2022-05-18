#Exercicio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar - Considerando cotação do dia 18/05/22 US$1,00 = R$4,97

n=float(input('Digite quantos reais você possui na carteira:'))
print('O valor em dolar é: US${:.2f}'.format(n/4.97)) #valor cotação do dia 18/05/22