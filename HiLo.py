# ==========================================
# HiLo
# ==========================================
# ==========================================
# Gabriel Lopes
# ==========================================

from random import randrange
escolha = randrange(1, 101)
tentativas = 0

while True:
    numero = int(input("advinha um número entre 1 e 100: "))
    tentativas +=1

    if numero > escolha:
        print('alto demais ')
    elif numero < escolha:
        print('baixo demais ')
    else:
        print('ACERTOU! ')
        print('número de tentativas: ', tentativas)
        break