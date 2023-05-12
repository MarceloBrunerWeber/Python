"""
Introdução ao try/except
try -> Tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# print(1234)
# print(456)
# int('a') # erro 

# (um erro = uma excessão)
# Estourar uma excessão significa que houve um erro em determinado lugar fazendo com que o código não execute a seguir.

# ----------------------------------------------------------------------------------------------------------------------------

numero_str = input('Vou dobrar o número que você digitar: ') 
# lembre que um input sempre voltará uma string

# print(f'O dobro de {numero_str} é {numero_str * 2}') 
# str * int = repetição

# ----------------------------------------------------------------------------------------------------------------------------

# como podemos corrigir ?

# numero_float = float(numero_str)
# print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')

# Pode parecer uma solução mas de nada serve. 
# O que aconteceria se o usuário mandasse uma letra no lugar de número ? Teriamos uma excessão e o código quebraria.
# Por isso sempre precisamos tratar um input de um usuário, poderiamos corrigi-lo utilizando try e except:

# ----------------------------------------------------------------------------------------------------------------------------

# no try ele irá executar o código mas assim que houver um erro ele irá pula-lo e executar o except: digite uma letra no input
try:
    numero_float = float(numero_str) # erro no código pois letra não pode ser convertida e pula o código do bloco.
    print('Float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número') # pula automaticamente para except

