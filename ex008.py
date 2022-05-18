#Exercicio 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

n=float(input('Digite um valor em metros para converte-lo em centimetros, milimetros e kilometros:'))
cm=n*100
mm=n*1000
km=n/1000
print('O valor digitado em metros é: {} \nO valor em centimetros é: {} \nO valor em milimetros é: {} \nO valor em Km é: {}'.format(n, cm, mm, km))