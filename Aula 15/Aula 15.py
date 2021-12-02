"""
Formatando Valores com indicadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^)(QUANTIDADE) ( TIPO - s, d ou f)

> - esquerda
< - direita
^ - centro
"""

num_1=1
print(f'{num_1:0>8}')
num_2=356
print(f'{num_2:0>8}')