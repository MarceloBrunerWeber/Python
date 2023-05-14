"""
Repetições:
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando um código não tem fim

Debugger é seu melhor amigo (não o quizzly).
"""
contador = 0 # quero contar de 1 em 1

while contador <= 100:
    contador += 1

    if contador == 6:
        print('não vou mostrar o 6')
        continue

    if contador >= 10 and contador <= 27:
        print('não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 30:
        break



print('Entrou no if e saiu!')
