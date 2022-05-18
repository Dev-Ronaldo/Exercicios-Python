#Desafio 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

n=int(input('Digite um valor em metros para converte-lo em centimetros e milimetros:'))
cent=n*100
mili=n*1000
print('O valor digitado em metros é: {} \nO valor em centimetros é: {} \nO valor em milimetros é: {}'.format(n, cent, mili))