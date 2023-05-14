# numero = input('Digite um número')
# numero2 = input('Digite um número')
# numero3 = input('Digite um número')
# numero4 = input('Digite um número')
# numero5 = input('Digite um número')

# numero_int = int(numero)
# numero_int2 = int(numero2)
# numero_int3 = int(numero3)
# numero_int4 = int(numero4)
# numero_int5 = int(numero5)

# numeros_int = [numero_int,numero_int2,numero_int3,numero_int4,numero_int5]
# numero_negativo = numero_int < 0 
# print(numero_negativo) 


numeros_negativos = []

try:
    numero = int(input("Digite um número: "))
    numero2 = int(input("Digite um número: "))
    numero3 = int(input("Digite um número: "))
    numero4 = int(input("Digite um número: "))
    numero5 = int(input("Digite um número: "))

    if numero < 0:
        numeros_negativos.append(numero)
    if numero2 < 0:
        numeros_negativos.append(numero2)
    if numero3 < 0:
        numeros_negativos.append(numero3)
    if numero4 < 0:
        numeros_negativos.append(numero4)
    if numero5 < 0:
        numeros_negativos.append(numero5)

    print(f"Numeros negativos digitados ao todo: {len(numeros_negativos)}")
except:
    print("Por favor putinha, insira um número")
