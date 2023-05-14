"""
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Por favor, digite seu nome: ')
idade = input('Digite sua idade: ')
nome_espacos = ' ' in nome
nome_invertido = f'{nome[::-1]}'
n = len(nome)
letra = nome

if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome_invertido}.')
    if nome_espacos == True:
            print('O seu nome contem espaços.')
    else:
            print('O seu nome não possui espaços.')
    print(f'Seu nome possui {n} letras.')
    print(f'A primeira letra do seu nome é "{letra[0]}".')
    print(f'A última letra do seu nome é "{letra[-1]}".')


else:
    print('Desculpe, você deixou campos vazios.')
