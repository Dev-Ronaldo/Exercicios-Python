#Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar - Considere US$1,00 = R$3,27

n=float(input('Digite quantos reais você possui na carteira:'))
print('O valor em dolar é: US${:.2f}'.format(n/3.27))