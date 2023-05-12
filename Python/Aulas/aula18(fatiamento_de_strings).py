"""
Fatiamento de strings:
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] 
i - inicio
f - fim (se o fim for omitido ele fiatiará até o fim do código)
p - passo (de quanto em quantos caracteres ele irá pular)
____________________________________________________________________________
Já a função len retornará a quantidade de caracteres dentro de uma string.  |
"""
variavel = 'Olá mundo'

print(len(variavel)) 
# Repare que contagem é diferente de Índice, aqui ele literalmente contou os caracteres, ou seja, 9.

print(variavel[5]) #

print(variavel[4:]) # Fim omitido, ou seja, seguirá até o fim do código.
print(variavel[:5]) # Também podemos omitir o inicio da string.

# Agora vamos supor que você quer do caractere 4 até o 7 "mund".
print(variavel[4:7]) # Como podemos ver, em python na maioria quando falamos de inicio e fim, o índice 
# pertencente ao fim não será incluído, para isso adicionaremos 1 número a mais:
print(variavel[4:8])

# e se pedirmos para nos mostrar pulando de 1 em 1 caractere ?
print(variavel[::1]) # Quando printamos uma palavra pulando de 1 em 1 temos a palavra por si só :skull:.
# E utilizando Índices negativos ?
# Índices negativos começam em contagem decrescente, ou seja, a palavra será escrita da direita para esquerda.
print(variavel[::-1]) 







