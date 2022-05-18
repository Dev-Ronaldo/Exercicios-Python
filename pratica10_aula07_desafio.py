#desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

n=float(input('Digite o valor do produto:'))
valorfinal=n*0.95
print('O valor do produto é: R${:.2f} \nO valor com desconto de 5% é: R${:.2f}'.format(n, valorfinal))
