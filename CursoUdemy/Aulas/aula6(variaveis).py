"""
Variáveis são usadas para salvar algo na memória do compiuter.
PEP8: inicie variáveis com letras minúsculas, pode-se usar números e underlines _.
O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um nome (variável) por exemplo:
nome_variavel = expressão
"""
nome_completo = "Juninho Silva Pinto"
soma_dois_mais_dois = 2+2
print(nome_completo, soma_dois_mais_dois)

# agora que sabemos como fazer variáveis podemos resolver o problema a seguir:

print(int("1"), type(int("1"))) # Na programação não se deve usar isso, várias vezes mesmo código escrito 
# faz ele ficar "sujo" adicione então uma variável no lugar para simplifica-lo

int_um = int("1")
print(int_um, type(int_um))
# Sempre use variáveis com nomes o mais autoexplicativos possíveis pois assim pessoas terão mais 
# facilidade ao ler o código

nome = "Luiz"
idade = 30
maior_de_idade = idade >= 18
print("Nome:",nome, "Idade:", idade)
print("É de maior ?:", maior_de_idade)