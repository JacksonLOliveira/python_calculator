# Calculadora em Python

print("\n******************* Python Calculator *******************\n \n")

def soma(x, y):
	return x + y

def sub(x, y):
	return x - y

def mult(x, y):
	return x * y

def div(x, y):
	return x / y

print('Bem vindo à calculadora!')
print('\n')

operation = input('Escolha as opções: \
\n\n1 - para adição \
\n2 - para subtração \
\n3 - para multiplicação \
\n4 - para divisão \
\n\nSua operação:   ')
print('\n')
fator1 = int(input('Qual o primeiro fator da operação?  '))
fator2 = int(input('Qual o segundo fator da operação?  '))


if operation == '1':

    adicao = ('{} + {} . '.format(fator1, fator2))
    resultado_adicao = soma(fator1, fator2)
    print('Sua adição é %s' %(adicao))
    print('O resultado da sua soma é %s .' %(resultado_adicao))

elif operation == '2':

    subtracao = ('{} - {} .'.format(fator1, fator2))
    resultado_subtracao = sub(fator1, fator2)
    print('Sua subtração é %s' %(subtracao))
    print('O resultado da sua subtração é %s .' %(resultado_subtracao))

elif operation == '3':

    multiplicacao = ('{} * {} .'.format(fator1, fator2))
    resultado_multiplicacao = mult(fator1, fator2)
    print('Sua multiplicação é %s' %(multiplicacao))
    print('O resultado da sua multiplicação é %s .' %(resultado_multiplicacao))

elif operation == '4':

    divisao = ('{} / {} . '.format(fator1, fator2))
    resultado_divisao = div(fator1, fator2)
    print('Sua divisão é %s' %(divisao))
    print('O resultado da sua divisão é %s .  ' %(resultado_divisao))

else:

  print('Você não digitou uma operação válida')