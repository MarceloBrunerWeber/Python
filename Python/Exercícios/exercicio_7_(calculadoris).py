
blabla = True
while blabla:
    try:
        d = float(input('Digite um número: '))
        operacao = input(f'Escolha a operação que deseja fazer:\n'
                        '[1] Soma\n'
                        '[2] Subtração\n'
                        '[3] Multiplicação\n'
                        '[4] Divisão\n'
                        '[5] Sair\n'
                        'Opção n°: ')
        e = float(input('Digite outro número: '))
        
        soma = d + e
        subtracao = d - e
        multiplicacao = d * e
        divisao = d / e
        
        if operacao == '1':
            print(f'{soma}')
        elif operacao == '2':
            print(f'{subtracao}')
        elif operacao == '3':
            print(f'{multiplicacao}') 
        elif operacao == '4':
            if e != 0:
                print(f'{divisao}')
            else:
                print('Não é possível dividir por zero.')
        elif operacao == '5':
            break
    except ValueError:
        print('Oops amigão, parece que você não digitou um número, vamos tentar dnv.')
        continue

    bla = input('Deseja continuar utilizando a calculadora ? [S]im [N]ão : ')
    if bla == 'S' or bla == 's':
        continue
    elif bla == 'N' or bla == 'n':
        blabla = False