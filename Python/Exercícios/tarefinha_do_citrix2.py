
n_petalas = int(input('Indique o número de pétalas: '))

bem_ou_mal = input('escolhe entre [B]em me quer ou [M]al me quer: ')

if bem_ou_mal == 'B':
    b= n_petalas % 2 == 0
    if b == True:  
        print('Mal me quer')
    elif b == False:
        print('Bem me quer')

elif bem_ou_mal == 'M':
    c = n_petalas % 2 == 0
    if c == True:  
        print('Bem me quer')
    elif c == False:
        print('Mal me quer')


print("Sara é uma filha da puta.")

