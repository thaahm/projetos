num = int(input('Digite um número: '))
tot = 0
for c in range (1, num +1):
    if num % c == 0:
        tot += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(' {} '.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Ele é primo!')
else:
    print('Ele não é primo!')
