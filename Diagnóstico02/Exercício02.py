import random

def computador_adivinha():
    print("Pense em um número entre 1 e 100. Vou tentar adivinhar!")
    
    numero_pensado = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 8

    while tentativas < max_tentativas:
        print("Minha tentativa: ", numero_pensado)
        resposta = input("O número está correto? Se sim, digite 'S'. Se maior, digite 'M'. Se menor, digite 'm': ")

        if resposta.lower() == 'c':
            print("Parabéns, eu acertei! (:-)")
            break
        elif resposta.lower() == 'm':
            numero_pensado = random.randint(1, numero_pensado - 1)
        elif resposta.lower() == 'mm':
            print(f"Você trapaceou! {numero_pensado} não é menor que meu chute {numero_pensado}.")
            break
        elif resposta.lower() == 'M':
            numero_pensado = random.randint(numero_pensado + 1, 100)
        elif resposta.lower() == 'mm':
            print(f"Você trapaceou! {numero_pensado} não é maior que meu chute {numero_pensado}.")
            break
        else:
            print("Entrada inválida. Por favor, digite 'C', 'M', 'm', 'MM' ou 'mm'.")
            continue

        tentativas += 1

    if tentativas == max_tentativas:
        numero_pensado_usuario = int(input("Que pena, acabaram minhas oportunidades (;-). Qual foi o número que você pensou? "))
        if numero_pensado_usuario == numero_pensado:
            print("Uma pena, não consegui adivinhar!")
        else:
            print("Você trapaceou! O número que você pensou {numero_pensado_usuario} não é igual ao meu último chute {numero_pensado}")

if __name__ == "__main__":
    computador_adivinha()