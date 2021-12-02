"""
Faça um programa que peça ao usuário para digitar um numero inteiro,
informe se esse numero é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro
"""

num1=input('Digite um número inteiro: ')
if num1.isdigit():
        num1=int(num1)

else:
       print()
       print("Digite um número válido")

resto=num1%2
if resto==0:
    print(f'O número {num1} é par')
else: print (f'o número {num1} é ímpar')
