"""
https://docs.python.org/pt-br/3/library/stdtypes.html

Imutaveis que vimos: str, int, float, bool
"""

string = 'luiz otávio' # o dado luiz otávio é imutável porem a variável string não mas como podemos provar que nosso dado str
# é imutavel ? 
# string[3] = 'ABC' # em teoria isso faria com que o z nosso índice 3 mudasse para ABC ou seja LuiABC Otávio mas como podemos ver
# ocorreu um erro que diz que str não suporta atribuição de itens
# então como podemos fazer para mudar o valor da variavel string ? não fazemos, nós teriamos que criar uma outra variavel
# outro_string = f'{string[:3]}ABC{string[4:]}'

# print(string[3])
# print(outro_string)

print(string.capitalize()) # .something = método, existem vários métodos podemos ver mais sobre eles no link acima ou digitando
# . após nossa variavel e lendo uma por uma até achar uma que satisfaça nossa necessidade.
# existem métodos específicos para str, int, float etc. etc.



