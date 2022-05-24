#Exercicio 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se las podem ou não formar um triângulo.
print('Verificador de retas para formar triângulos!')
r1=float(input('digite o tamanho da reta 1:'))
r2=float(input('digite o tamanho da reta 2:'))
r3=float(input('digite o tamanho da reta 3:'))

if r1<(r2+r3) and r2<(r1+r3) and r3<(r1+r2):  #As retas não podem ser maiores que a soma das outras duas retas!
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')