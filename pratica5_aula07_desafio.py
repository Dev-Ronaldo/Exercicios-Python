#Desafio 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1=int(input('Digite a primeira nota:'))
n2=int(input('Digite a segunda nota:'))
media=(n1+n2)/2
print('As notas do aluno foram: {} e {} \nE a média final é: {}'.format(n1, n2, media))

