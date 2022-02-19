branco = " "
token = ["x", "o"]


def criarBooard():
    bordas = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco],
    ]
    return bordas


def printBoard(bordas):
    for i in range(3):
        print("|".join(bordas[i]))
        if (i < 2):
            print(".....")


def getInputValido(mensagem):
    try:
        n = int(input(mensagem))
        if (n >= 1 and n <= 3):
            return n - 1
        else:
            print("Seu numero não pode ser menor que 0 e nem maior que 3")
            return getInputValido(mensagem)
    except:
        print("numero não válido!!")
        return getInputValido(mensagem)


def verificaMovimento(bordas, i, j):
    if (bordas[i][j] == branco):
        return True
    else:
        return False


def fazMovimento(bordas, i, j, jogador):
    bordas[i][j] = token[jogador]


def verificaGanhador(bordas):
    for i in range(3):  # linha
        if (bordas[i][0] == bordas[i][1] and bordas[i][1] == bordas[i][2] and bordas[i][0] != branco):
            return bordas[i][0]

    for i in range(3):  # coluna
        if (bordas[0][i] == bordas[1][i] and bordas[1][i] == bordas[2][i] and bordas[0][i] != branco):
            return bordas[0][i]

    # diagonal principal
    if (bordas[0][0] != branco and bordas[0][0] == bordas[1][1] and bordas[1][1] == bordas[2][2]):
        return bordas[0][0]

    # diagonal secundária
    if (bordas[0][2] != branco and bordas[0][2] == bordas[1][1] and bordas[1][1] == bordas[2][0]):
        return bordas[0][2]

    for i in range(3):
        for j in range(3):
            if (bordas[i][j] == branco):
                return False
    return "EMPATE"
