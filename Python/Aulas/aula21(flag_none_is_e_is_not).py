"""
Flag (Bandeira) - Marcar um local
none - Não valor
is e is not - é ou não é (tipo, valor, identidade)
id - identidade adereçada à memória (endereço que percorre para buscar da memória e trazer para o python)
"""
# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

#------------------------------------------------------------------------------------------------------------------

condicao = True
passou_no_if = None # a não atribuição de um valor

if condicao:
    passou_no_if = True # flag "fincando a bandeira" afirmando que agora que nossa condição entrou no if a 
#nossa variável que não tinha valor possuirá um (o da flag).
    print('Faça algo')
else:
    print('Não faça algo')

# print(passou_no_if, passou_no_if is None) # checa se passou_no_if é none, se sim sairá True
# print(passou_no_if, passou_no_if is not None) # checa se passou_no_if não é um none, caso seja sairá False

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')
