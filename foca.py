
palavra = "PYTHON"
letras_descobertas = []
erros = 0
limite_erros = 6

while erros < limite_erros:
    print("\n===== JOGO DE ADIVINHAÇÃO =====")

    for letra in palavra:
        if letra in letras_descobertas:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print("\nErros:", erros)

    tentativa = input("Digite uma letra: ").upper()

    if tentativa in letras_descobertas:
        print("Você já tentou essa letra!")

    elif tentativa in palavra:
        letras_descobertas.append(tentativa)
        print("Acertou!")

    else:
        erros += 1
        print("Letra incorreta!")

    if all(letra in letras_descobertas for letra in palavra):
        print("\nParabéns! Você venceu!")
        break

if erros == limite_erros:
    print("\nVocê perdeu!")

print("A palavra era:", palavra)
