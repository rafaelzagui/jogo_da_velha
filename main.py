from jogo_da_velha import criarBoard, fazerMovimento, getInputValido, \
    printarBoard, verificarGanhador, verificarMovimento
import random

from minmax import movimentoIA

jogador = 0  # jogador 1
board = criarBoard()
ganhador = verificarGanhador(board)
while not ganhador:
    printarBoard(board)
    print("===================")
    if jogador == 0:
        i, j = movimentoIA(board, jogador)
    else:
        i = getInputValido("Digite a linha: ")
        j = getInputValido("Digite a coluna: ")

    if verificarMovimento(board, i, j):
        fazerMovimento(board, i, j, jogador)
        jogador = (jogador + 1) % 2
    else:
        print("A posicao informada está preenchida")

    ganhador = verificarGanhador(board)

print("===================")
printarBoard(board)
print("Ganhador = ", ganhador)
print("===================")
