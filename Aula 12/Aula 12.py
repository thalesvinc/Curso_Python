num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

if num1.isdigit():
    num1=int(num1)
    num2=int(num2)

    print(num1+num2)
else:
    print('Digite apenas caracteres válidos')