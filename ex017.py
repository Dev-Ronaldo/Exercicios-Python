#Exercicio 17 - Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo retangulo, calculo e mostre o comprimento da hipotenusa
import math
c1=float(input('Digite o cateto adjacente:'))
c2=float(input('Digite o cateto oporto:'))
hyp= math.sqrt(c1*c1 + c2*c2)


print('A medida da hipotenusa é: {}\n {}'.format(hyp, math.hypot(c1,c2)))

#Utilizei os 2 metodos para verificar se o valor estava correto