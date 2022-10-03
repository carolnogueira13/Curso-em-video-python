x = input('Digite algo: ')
print('O tipo primitivo desse valor é {}' .format(type(x)))
print('Só tem espaços? {}' .format(x.isspace()))
# Também pode escrever assim print('Só tem espaços?', x.isspace())
print('É um número? {}' .format(x.isnumeric()))
print('É alfabético? {}' .format(x.isalpha()))
print('Está em maiúsculas? {}' .format(x.isupper()))
print('Está em minúsculas? {}' .format(x.islower()))
print('Está capitalizada? {}' .format(x.istitle()))








