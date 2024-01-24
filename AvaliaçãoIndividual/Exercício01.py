import numpy as np
print(np.__version__)

def geradorImagens(height=720, width=1280):
    return np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)

def solicitarParametros():
    altura = int(input("Digite a altura da imagem (deixe em branco para padrão 720): ") or 720)
    largura = int(input("Digite a largura da imagem (deixe em branco para padrão 1280): ") or 1280)
    return altura, largura

altura, largura = solicitarParametros()

imagem_teste = geradorImagens(altura, largura)

print("------")
print("\nTeste:")
print("------")
print(geradorImagens().shape) 
print(geradorImagens(10).shape) 
print(geradorImagens(10,10).shape) 

print(f"Dimensões da imagem gerada: {imagem_teste.shape}")
print("\n---------------------------------")
print("Imagem RGB gerada aleatoriamente:")
print("---------------------------------")
print(imagem_teste)
