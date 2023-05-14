"""
Interpolação básica de strings (mais um método de formatação)

s    - string
d, i - int
f    - float
x, X - Hexadecimal (ABCDEF0123456789) números formados de letras até A até F e de 1 até 9.
"""

nome = 'Luiz'
preco = 1000.9283823
# variavel = 'Luiz, o preço total foi R$1000.95' como fazer isso usando de interpolação ? veja a seguir:
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08x' % (1500, 1500))