
# Exercício IMC

nome = "Marcelinho-senpai"
altura = 1.78
peso = 67
imc = peso / (altura * altura)

# f-strings
linha_1 = f"{nome} tem {altura:.2f} de altura"  
# :.xf x = número de casas decimais que serão mostradas, f = float

linha_2 = f"pesa {peso} quilos e seu IMC é: {imc:.2f}"

print(linha_1)
print(linha_2)

a = 'A'
b = 'B'
c = 1.1
string = 'a={nome1} b={1} c={nome1:.2f}'

"""
{} vazios fazem com que os argumentos sejam atribuidos em ordem, porem se utilizarmos
um número, podemos nos libertar da ordem e começar a escolher qual queremos.
"""
formato = string.format(a, b, nome1=c) 

"""
nome1 é um parâmetro nomeado (tudo que vem após também precisará ser nomeado), 
para utiliza-lo a partir de agora tenho que me referir a ele na string utilizando o seu nome (nome1) 
já os não nomeados (a, b) são chamados de argumentos  tudo o que possui uma ordem começa do 0.
"""
print(formato)