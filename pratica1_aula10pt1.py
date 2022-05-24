n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))

m = (n1+n2+n3)/3

print ('A sua média é: {:.1f}'.format(m))

if m>= 6:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')