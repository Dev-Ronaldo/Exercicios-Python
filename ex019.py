#Exercicio 19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice
n1=str(input('Digite o nome do primeiro aluno:'))
n2=str(input('Digite o nome do segundo aluno:'))
n3=str(input('Digite o nome do terceiro aluno:'))
n4=str(input('Digite o nome do quarto aluno:'))

print('O aluno escolhido é: {}'.format(choice([n1,n2,n3,n4])))

