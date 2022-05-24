#Exercicio 034 - Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
#Para salarios superiores a R$1250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é 15%.

salario=float(input('Digite o salario do funcionário:'))

if salario>1250:
    salario2=salario+(salario*0.10)
    print('O aumento foi de 10%\nO salario com aumento é: R${:.2f}'.format(salario2))
else:
    salario2=salario+(salario*0.15)
    print('O aumento foi de 15%\nO salario com aumento é: R${:.2f}'.format(salario2))