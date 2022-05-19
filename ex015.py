#Exercicio 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

dias=float(input('Digite quantos dias o carro foi alugado:'))
km=float(input('Digite quantos Km foram rodados com o carro:'))
valor=(dias*60)+(km*0.15)

print('O carro foi alugado por {} dias e foram rodados {} Km\n O valor total é: R${:.2f}'.format(dias, km, valor))