"""
Formatação básica de strings
s - strings
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABCD'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel:->10}')
print(f'{variavel:-<10}')
print(f'{variavel:-^10}')

print(f'{1000.18723678263:.2f}')

print(f'O hexadecimal de 1500 é {1500:08x}')