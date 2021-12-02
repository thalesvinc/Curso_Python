while True:
    print()
    num_1=input('Digite um número: ')
    num_2=input ('Digite outro número: ')
    operador=input('Digite um Operador (+ - / *):  ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa de digitar um número válido')
        continue
    num_1= int(num_1)
    num_2= int(num_2)

    if operador == '+':
        print (num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Digite um operador válido')


