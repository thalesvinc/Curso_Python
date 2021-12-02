"""
Condições IF, ELIF e ELSE
Operadores Relacionais == > >= < <=
!= Diferente
"""
nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")
idade_menor = 18
idade_maior= 70
idade =int(idade)
if idade>=idade_menor and idade<=idade_maior :
    print (f'olá {nome} você já está apto a dirigir')
else:
    print(f'Olá {nome} infelizmente você não está apto a dirigir')