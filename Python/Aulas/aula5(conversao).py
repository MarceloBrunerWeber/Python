# Conversão de tipos, coerção.
"""
type convertion, typecasting, coercion é o ato de converter um tipo em outro, tipos imutáveis e primitivos: 
str, int, float, bool
"""
print(1+2)
print('a'+'b') # 2 strings se concatenarão
# Print("1"+2) acontecerá um erro, só se pode concatenar 2 do mesmo tipo

print('1', type('1'))
print(int('1'), type(int('1')))

# Sendo assim agora conseguimos fazer a seguinte soma:
print(int("1")+2)
# Podemos também fazer o contrário:
print(str(1)+"b")
 
# Mas o que aconteceria se fizessemos o mesmo porém transformando em float ao invés de int ?
print(float("1")+2) #como podemos ver o resultado será transformado em um float !


