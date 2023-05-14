# Complexidade do código, algumas boas práticas de programação e como podemos pensar para escrever programas para outras
# pessoas e não para o computador.
# Na maioria das vezes estamos escrevendo códigos para outras pessoas, sua equipe no trabalho ou até mesmo para
# você utiliza-lo mais tarde. Sendo assim, é muito importante escrever um código "Limpo" e que consiga ser entendido.

"""
CONSTANTE = "Variáveis" que não vão mudar, no python constantes não existem, porém, existe uma convenção entre devs que
se alguém escrever algo em maiúsculo significa que não se deve atribuir outros valores a ela pois é uma CONSTANTE.

Muitas condições mesmo if (ruim), muitas vezes pode ficar muito difícil de entender se algo vai ou não entrar 
no if quando setem várias condições então evite para que seja de fácil identificação, as pessoas tem que conseguir ler 
seu código de forma simples. 
--- Trabalhamos para pessoas não máquinas. ---

    <- contagem de complexidade (ruim) quanto mais afastado da margem mais blocos dentro de blocos estaremos utilizando
isso fará com que nosso código se torne complexo e complexidade não é bom, mantenha-o simples! 
--- Simples é melhor do que complexo. ---
"""
velocidade = 60 # Velocidade atual do carro.
local_carro = 100 # Local em que o carro está na estrada.

RADAR_1 = 60 # Velocidade máxima do radar 1.
LOCAL_1 = 100 # Local onde o radar 1 se encontra.
RADAR_RANGE = 1 # A distância onde o radar pega (frente e atrás, ou seja, local 99 e 101)

lado_n_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
lado_s_radar_1 = local_carro <= (LOCAL_1 + RADAR_RANGE)
velocidade_carro_passou_do_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = lado_n_radar_1 and lado_s_radar_1
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_do_radar_1

if velocidade_carro_passou_do_radar_1:
    print('Velocidade do carro passou do Radar 1.')

if carro_passou_radar_1:
    print('Carro passou no radar 1.')

if carro_multado_radar_1:
    print('Carro multado no Radar 1.')

