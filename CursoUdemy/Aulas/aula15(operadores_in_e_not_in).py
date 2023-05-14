# Operadores in e not in
# Strings são alteráveis
# 0 1 2 3 4 5 Indices
# O t á v i o
#-6-5-4-3-2-1

nome = 'Otávio' # como podemos acessar o "á" ?
print(nome[2]) # utilizando do [x] x= número do índice que queremos.
print(nome[-4]) # podemos também utilizar do índice pela sua forma negativa.

print(10 * '--')
# Visto isso podemos dizer que "Strings em Python são inteiraveis".
# partiremos então para o uso do in:

print('á' in nome) # Ele irá rodar o código nome à procura de uma letra 'á' e se for encontrada ele retornara como True.
print('vio' in nome)
print('y' in nome) # Se a letra não for encontrada ele retornará como False.
# podemos fazer o mesmo utilizando do not in, que irá retornar o oposto do in.

print(10 * '--')

print('á' not in nome) # Ele irá rodar o código nome à procura de uma letra 'á' e se for encontrada ele retornara como False.
print('vio' not in nome)
print('y' not in nome) # Se a letra não for encontrada ele retornará como True.

print(10 * '--')
# com isso podemos fazer um código que nos dirá se existe algo dentro de algo:

nome2 = input('Digite seu nome: ')
encontre = input('Digite o que deseja encontrar: ')

if encontre in nome2:
    print(f'{encontre} está em {nome2}')
else:
    print(f'{encontre} não está em {nome2}')




