#Exercicio 023 - Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados. Ex: Digite um numero 1834  unidade: 4, dezena 3, centena 8, milhar 1

n=int(input('Digite um numero entre 0 e 9999:'))
n1=str(n)

#print('Unidade= {}\nDezena= {}\nCentena= {}\nMilhar= {}'.format(n1[3], n1[2], n1[1], n1[0]))
#este caso não funciona quando o numero digitado não tem um dos itens por exemplo: 12
#pode-se fazer então:

u=n // 1 % 10
d=n // 10 % 10
c=n // 100 % 10
m=n // 1000 % 10

print('\n\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d, c, m))