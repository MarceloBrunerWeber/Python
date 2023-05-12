# Tipos int e float

"""
int -> Número inteiro.
O tipo int representa qualquer número seja ele positivo ou negativo.
int sem sinal será considerado positivo por padrão.
"""
print(11, 0) # int
print(-11, 0) # int

"""
float -> Número com ponto flutuante.
O tipo float representa qualquer número positivo ou negativo que possua ponto flutuante (vírgula).
float sem sinal será considerado positivo por padrão.
"""
print(1.1, 11.11)
print(0.0, -11.11)

# A função type mostra o tipo que o python aderiu ao valor

print(1.2,"é da",type(1.2))
print(12,"é da",type(12))
print("blabla é da",type("blabla"))