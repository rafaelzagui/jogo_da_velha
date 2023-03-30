from jogo_da_velha import branco, token, verificarGanhador


# Retorna o melhor movimento que pode ser feito
def movimentoIA(board, jogador):
    possibilidades = getPosicoes(board)
    melhorValor = None
    melhorMovimento = None
    # percorrendo a matriz e vendo todos as possibilidades de movimento
    for possibilidade in possibilidades:

        board[possibilidade[0]][possibilidade[1]] = token[jogador]  # fazendo o movimento
        valor = miniMax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco  # limpando as posições dps de jogar

        if melhorValor is None:
            melhorValor = valor
            melhorMovimento = possibilidade
        elif jogador == 0:
            if valor > melhorValor:
                melhorValor = valor
                melhorMovimento = possibilidade

        elif jogador == 1:
            if valor < melhorValor:
                melhorValor = valor
                melhorMovimento = possibilidade

    return melhorMovimento[0], melhorMovimento[1]


# Pega todas as posições na matrix que estão vazias
def getPosicoes(board):
    posicoes = []  # Lista de posições
    for i in range(3):  # percorrer a linha da matriz
        for j in range(3):  # Percorrer a coluna
            if board[i][j] == branco:
                posicoes.append([i, j])

    return posicoes


score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1
}


def miniMax(board, jogador):
    #  Verifica se alguem já não ganhou a partida
    ganhador = verificarGanhador(board)
    if ganhador:
        return score[ganhador]
    jogador = (jogador + 1) % 2  # Trocar o jogador se o jogador for 0 (0 mais 1) o resto da divisão é 1 então
    # jogador 1 joga se o jogador 1 estiver a jogar 1 + 1= 2 proximo jogador é o 0

    possibilidades = getPosicoes(board)
    melhorValor = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]  # fazendo o movimento
        valor = miniMax(board, jogador)  # Pegar o valor
        board[possibilidade[0]][possibilidade[1]] = branco  # Limpar o baord novamente

        # Verifica qual jogador que é
        if melhorValor is None:
            melhorValor = valor
        elif jogador == 0:
            if valor > melhorValor:
                melhorValor = valor
        elif jogador == 1:
            if valor < melhorValor:
                melhorValor = valor

    return melhorValor  # Retorna o melhor movimento que ela pode fazer
