"""
if/ elif      / else
se/ se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == "entrar":  
    # se a condição for true ele executará o código de dentro da condição, irá pular todos os elifs e o else e irá direto
    # para o código fora destas condições
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem "entrar" e nem "sair".')

print('Estou fora.')


"""

condicao = False
condicao2 = True 
condicao3 = True
condicao4 = False
if condicao:
    print('Esta é a condição 1.')
elif condicao2: 
# assim que o elif que bate os requisitos é executado ele sai do bloco não importante se o próximo também é True ou não
    print('Esta é a condição 2.') 
elif condicao3:
    print('Esta é a condição 2.')
elif condicao4:
    print('Esta é a condição 2.')
else: 
    print('Este é o else do primeiro if.')

if 10 == 10: # podemos ter um if sozinho porém não podemos ter elif nem else sozinhos, eles dependem do if.
    print('Outro if.')

print('Fora do if.')

