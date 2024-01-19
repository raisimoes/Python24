import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)

    print("Pensei em um número entre 1 e 100. Tente adivinhar!")

    tentativas = 0
    max_tentativas = 8

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Digite um número válido")
            continue
        
        if palpite < numero_secreto:
            print("Não, o número é maior (:-(")
        elif palpite > numero_secreto:
            print("Não, o número é menor (:-0)")
        else:
            print("Parabéns, você acertou (:-)")
            break

        tentativas += 1

    if tentativas == max_tentativas:
        print("Lamento, acabaram suas oportunidades (;-)")
        print("O número correto era:", numero_secreto)

if __name__ == "__main__":
    jogo_adivinhacao()