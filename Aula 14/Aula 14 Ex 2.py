"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada
ex.Bom dia 0-11; Boa tarde 12-17 e Boa Noite 17-23
"""

nome = input('Qual é o seu nome?: ')
hora = input('Que horas são?(hh):')

if hora.isdigit():
    hora=int(hora)
    if hora<0 or hora>23:
        print(f'Olá {nome}, favor digitar um horário entre 0 e 23')
    if hora==0:
        print(f'Olá {nome}; agora é meia noite! hora de ir dormir, boa noite!')
    if hora<11 and hora != 0:
        print(f'olá {nome}; agora são {hora}h da manhã! tenha um bom dia!')
    elif hora<17 and hora!=0:
        print(f'Olá {nome}; agora são {hora}h da tarde! tenha uma boa tarde!')
    elif hora<23 and hora != 0:
        print(f'Olá {nome}; agora são {hora}h da noite! tenha uma boa noite!')

else:
    print(f' Olá {nome}! por favor; digite uma hora válida entre 0 e 23')
