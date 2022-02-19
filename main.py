from jogo import criarBooard, printBoard, getInputValido, verificaGanhador, fazMovimento, verificaMovimento
from minimax import movimentoIA

jogador = 0  # jogador 1
bordas = criarBooard()
ganhador = verificaGanhador(bordas)
while (not ganhador):
    printBoard(bordas)
    print("_____________")
    if(jogador == 0):
        i,j = movimentoIA(bordas, jogador)
    else:
        i = getInputValido("Digite a linha: ")
        j = getInputValido("Digite a coluna: ")

    if (verificaMovimento(bordas, i, j)):
        fazMovimento(bordas, i, j, jogador)
        jogador = (jogador + 1) % 2
    else:
        print("A posição informada já está ocupada")

    ganhador = verificaGanhador(bordas)

print("-------------")
printBoard(bordas)

if(ganhador == "EMPATE"):
    print("\nO JOGO EMPATOU")
else:
    print("\nO GANHADOR FOI O JOGADOR: ", ganhador)
print("-------------")

if(ganhador == "x"):
    print("IA: EU SOU O MELHOR!!")
else:
    print("IA: (ノ｀Д´)ノ彡┻━┻")
print("-------------")