n1=int(input('Digite um valor:'))
n2=int(input('Digite outro valor:'))
s= n1 + n2
m= n1 * n2
d= n1 / n2
di = n1 // n2
e= n1 ** n2

print('A soma é: {} \no produto é: {} \na divisão é: {} \na divisão inteira é: {:.3f} \na potência é: {}'.format(s, m, d, di, e, end=''))
