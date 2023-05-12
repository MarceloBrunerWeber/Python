# input faz uma pergunta para o usuário e sempre retornará uma string
# nome = input('Qual é o seu nome? ')
# print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)
# print(f'A soma dos números é: {numero_1 + numero_2}') #
#  o resultado sairá errado pois um input sempre retornará str, para funcionar você tem que converter em int

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
"""
vendo a solução acima você pode ter pensado, mas porque não converter para int diretamente no input ?
a resposta é simples, e se o usuário digitar algo que não possa ser transformado em int como uma letra ?
exato, o usuário estará matando o código ali mesmo logo no inicio por isso será melhor se adicionarmos esse passo a uma outra
variável onde poderemos estar verificando melhor usando metodos que veremos logo logo
"""
