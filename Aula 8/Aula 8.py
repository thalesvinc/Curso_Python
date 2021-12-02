"""
Entrada de Dados
"""
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
ano_nascimento= input("Qual o seu ano de nascimento? ")
print()
print(f"{nome} tem {idade} anos de idade e completará até o final do ano {2021-(int(ano_nascimento))} anos")