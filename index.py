número = int(input('Me diga um número qualquer:'))
resultado = número % 2
print('O resultado foi {}'. format(resultado))
if resultado == 0:
    print('Onúmero {} é PAR'.format(número))
else:
    print('Onúmero {} é ÍMPAR'.format(número))