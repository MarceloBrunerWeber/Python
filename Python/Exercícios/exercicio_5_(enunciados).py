"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar.
caso o usuário não digite um número inteiro, informe que ele não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    numero_par = numero_int % 2 == 0
    
    print(f'{numero_int} é um número inteiro!')
    if numero_par:
        print(f'{numero_int} é um número par!')
    else:
        print(f'{numero_int} é um número impar!')
except:
    print(f'Por favor, insira um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Olá, que horas são? ')
horas_do_dia = [1,2,3,4,5,6,7,8,9,10,11]
horas_da_tarde = [12,13,14,15,16,17]
horas_da_noite = [18,19,20,21,22,23]
try:
    horas = int(hora)
    if horas in horas_do_dia:
        print(f"Bom dia, agora são {horas} da manhã.")
    elif horas in horas_da_tarde:
        print(f"Boa tarde, agora são {horas} horas.")
    elif horas in horas_da_noite:
        print(f"Boa noite, agora são {horas} horas.")
    else:
        print("Por favor, insira uma hora válida entre 0 e 23.")
except:
    print('Por favor, insira uma hora válida.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
nome = input('Por favor, digite seu primeiro nome: ')
curto = len(nome) <= 4
medio = len(nome) <= 6

if curto:
    print('Seu nome é curto.')
elif medio:
    print('Seu nome é de tamanho médio.')
else:
    print('Seu nome é muito grande.')
