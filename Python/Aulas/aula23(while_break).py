"""
Repetições:
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando um código não tem fim
"""
condicao = True

# enquanto nossa condição for verdadeira ele ira entrar no bloco, quando acabar de executa-lo ele voltará ao começo do while
# para ver se a condição continua verdadeira e se sim continuará todo esse loop até que ela seja falsa em algum momento
while condicao:  
    nome = input('Digite o seu nome: ') #
    print(f'Seu nome é {nome}.')
    # break serve para sair de um bloco por ex:
    if nome == 'sair':
        break # como utilizamos o break dentro de um bloco if ele irá sair para nosso bloco while ou seja voltará para o loop
    
print('batatinha')