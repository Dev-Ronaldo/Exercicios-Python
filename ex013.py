#Exercicio 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

n = float(input('Digite o salario atual do funcionário:'))
valorfinal = n * 1.15

print('O valor do salário atual é: R${:.2f} \nO valor do salário após o aumento de 15% é: R${:.2f}'.format(n, valorfinal))