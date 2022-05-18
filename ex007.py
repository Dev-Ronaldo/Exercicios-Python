#Exercicio 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota:'))
media=(n1+n2)/2
print('As notas do aluno foram: {:.2f} e {:.2f} \nE a média final é: {:.2f}'.format(n1, n2, media))