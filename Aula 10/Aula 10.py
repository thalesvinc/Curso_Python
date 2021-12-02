"""
Operadores lógicos
and, or, not
in e not in
"""

usuario = input('Nome de usuário: ')
senha = input('senha do usuário: ')

usuario_bd = 'thalesvinc'
senha_bd='12345'

if usuario_bd==usuario and senha_bd==senha:
    print()
    print('Senha e usuario corretos')
else:
    print()
    print('verificar usuário e senha')
