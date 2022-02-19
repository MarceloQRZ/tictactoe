from jogo import branco, token, verificaGanhador


def movimentoIA(bordas, jogador):
    possibilidades = getPosicoes(bordas)
    melhorValor = None
    melhorMovimento = None

    for possibilidade in possibilidades:
        bordas[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(bordas, jogador)
        bordas[possibilidade[0]][possibilidade[1]] = branco

        if (melhorValor is None):
            melhorValor = valor
            melhorMovimento = possibilidade
        elif (jogador == 0):
            if (valor > melhorValor):
                melhorValor = valor
                melhorMovimento = possibilidade
        elif (jogador == 1):
            if (valor < melhorValor):
                melhorValor = valor
                melhorMovimento = possibilidade

    if(melhorValor*100 == 100):
        print("IA: NEM VEM, EU VOU GANHAR!")

    return melhorMovimento[0], melhorMovimento[1]


def getPosicoes(bordas):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if (bordas[i][j] == branco):
                posicoes.append([i, j])

    return posicoes


score = {
    "EMPATE": 0,
    "x": 1,
    "o": -1
}


def minimax(bordas, jogador):
    ganhador = verificaGanhador(bordas)
    if (ganhador):
        return score[ganhador]
    jogador = (jogador + 1) % 2

    possibilidades = getPosicoes(bordas)
    melhorValor = None
    for possibilidade in possibilidades:
        bordas[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(bordas, jogador)
        bordas[possibilidade[0]][possibilidade[1]] = branco

        if (melhorValor is None):
            melhorValor = valor

        elif (jogador == 0):
            if (valor > melhorValor):
                melhorValor = valor

        elif (jogador == 1):
            if (valor < melhorValor):
                melhorValor = valor

    return melhorValor
