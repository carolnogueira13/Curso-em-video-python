num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
s = num1 + num2
m = num1 * num2
d = num1 / num2
di = num1 // num2
e = num1 ** num2
print('A soma é {}, o produto é {} e a divisão é {:.3f}!' .format(s, m, d), end=' ')
print('A divisão inteira é {} e a potência é {}!' .format(di, e))


