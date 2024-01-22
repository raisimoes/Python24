import pandas as pd

def main ():
    print("--------------------------------------")
    print("Enquete: melhor jogador de cada partida")
    print("--------------------------------------")

    votos = []
    jogador = int(input("\n Digite o número do jogador votado, entre 1 e 23 (Para encerrar digite 0): "))

    while jogador != 0:
        if 1 <= jogador <= 23:
            votos.append(jogador)
        else:
            print("Digite um valor entre 1 e 23 ou 0 para encerrar.")
            
        jogador = int(input("\n Digite o número do jogador votado, entre 1 e 23 (Para encerrar digite 0): "))

        if len(votos) > 0:
            contar_votos(votos)

def contar_votos(votos):
    df = pd.DataFrame(votos, columns=['Jogador'])
    contagem_votos = df['Jogador'].value_counts().reset_index()
    contagem_votos.columns = ['Jogador', 'Votos']

    total_votos = contagem_votos['Votos'].sum()

    contagem_votos['%'] = (contagem_votos['Votos'] / total_votos) * 100
    contagem_votos = contagem_votos.sort_values(by='Jogador')

    melhor_jogador = contagem_votos.loc[contagem_votos['Votos'].idxmax()]

    print("----------")
    print("RESULTADO:")
    print("----------")
    print(f"Foram computados {total_votos} votos.")
    print(contagem_votos.to_string(index=False))
    print(f"\nO melhor jogador foi o número {melhor_jogador['Jogador']}, "
          f"com {melhor_jogador['Votos']} votos, com {melhor_jogador['%']:.1f}% do total de votos.")
    
if __name__ == "__main__":
    main()