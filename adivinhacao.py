print("**********************************")
print("Bem vindos ao jogo de adivinhação!")
print("**********************************")

numero_secreto = 43
total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas:
    print("Tentativa:", rodada, "de", total_de_tentativas)
    chute = input("Digite o seu número: ")
    print("Você digitou", chute)
    chute = int(chute)
    
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou o número secreto!")
    elif maior:
        print("Você errou.O seu chute foi maior que o número secreto")
    elif menor:
        print("Você errou.O seu chute foi menor que o número secreto")
    rodada = rodada + 1

print("Fim do jogo")