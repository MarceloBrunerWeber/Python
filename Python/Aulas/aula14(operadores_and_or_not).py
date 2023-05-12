# Operadores Lógicos and (e) or (ou) not (não):
"""
and - Todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.

São considerados falsys (que você já viu) os seguintes: 0, 0.0, '', False. 
Qualquer coisa fora disso será considerado truthy: 1, 0,1, ' ', True.

Também existe o tipo None que é usado para representar um não valor (que não existe).
"""
#---------------------------------------------------------------------------------------------------

# and:
# Começa a checar e para quando acha um false, não seguindo em frente também retorna o valor da condição falsa.
# o código a seguir não é um sistema, é só uma forma de entender melhor a lógica por trás da matéria em questão.

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123'

if entrada == 'E' and senha_digitada == senha_permitida: 
# como podemos ver o and é basicamente usado quando precisamos checar mais de uma condição.
    print('Entrar')
else:
    print('Sair')


#---------------------------------------------------------------------------------------------------


"""
or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
"""
entrada2 = input('[E]ntrar [S]air: ')
senha_digitada2 = input('Senha: ')

senha_permitida2 = '123'

# if entrada2 == 'E' or entrada2 == 'e' and senha_digitada2 == senha_permitida2: 
# antes tinhamos o problema de que, se digitassemos em minúsculo ele entraria no else automaticamente
# porém agora utilizando do "or" podemos resolver isso. Porém criamos outro problema
# conforme o código vai ficando maior e vamos adicionando mais e mais condições o código pode acabar ficando ambiguo
# por isso podemos utilizar do que aprendemos na aula 9 (prioridade dos operadores) para obrigar o código a fazer a leitura
# de certa parte primeiro e só então seguir com nosso código tudo da mesma linha por exemplo 

if (entrada2 == 'E' or entrada2 == 'e') and senha_digitada2 == senha_permitida2: 

    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True or False or True) # repare que ele irá parar de ler o código assim que ler o primeiro True.

senhazinha = input('Senha: ') or 'Sem senha' 
print(senhazinha)
# perceba que ao não dar um input será False mas a nossa condição a partir do or será um True sendo assim ele irá printar
# Sem senha, ou seja, criamos um if utilizando apenas de um or.

#---------------------------------------------------------------------------------------------------

"""
not - usado para inverter expressões.
not True = False
not False = True
"""
senha3 = input('Senha: ')

# if senha3 == '1234':
#     print('Você entrou, parabéns!')
# else:
#     print('Senha incorreta.')
# ou também poderiamos utilizar da seguinte forma:
if not senha3:
    print('Senha incorreta.')