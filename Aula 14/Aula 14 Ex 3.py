"""
Faça um programa que peça seu primeiro nome. se o nome tiver 4 letras ou menos escreva: "seu nome é muito curto";
se tiver entre 5 e 6 letras, escreva "seu nome é normal"; maior que 6 letras "seu nome é muito grande"
"""

nome = input("Qual é o seu nome?  ")
letras = len(nome)

if letras<= 4:
    print(f'olá {nome} o seu nome tem {letras} letras e é considerado muito curto')
elif letras<=6:
    print (f' olá {nome} seu nome tem {letras} letras e é considerado de um tamanho normal')
else:
    print (f' olá {nome} seu nome tem {letras} letras e é considerado muito grande')

