"""
Iterando strings com while
"""
#        0123456789
#nome = 'Marcelinho'  # Iterável
#       10987654321
nome = input('Digite seu nome: ')
indice = 0 

print(f'Olá {nome}, seu nome letra por letra é:')

while indice <= len(nome):
    print(nome[indice])
    indice += 1
