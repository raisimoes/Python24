import numpy as np
print(np.__version__)

def geradorImagens(height=720, width=1280):
    return np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)

def converter_tons_cinza(imagem_rgb):
    imagem_tons_cinza_media = np.mean(imagem_rgb, axis=-1, dtype=np.uint8)
    imagem_tons_cinza_ntsc = np.dot(imagem_rgb, [0.299, 0.587, 0.114]).astype(np.uint8)
    return imagem_tons_cinza_media, imagem_tons_cinza_ntsc

altura = int(input("Digite a altura da imagem (deixe em branco para padrão 720): ") or 720)
largura = int(input("Digite a largura da imagem (deixe em branco para padrão 1280): ") or 1280)

imagem_teste = geradorImagens(altura, largura)

imagem_media, imagem_nstc = converter_tons_cinza(imagem_teste)

print(f"Dimensões da imagem gerada: {imagem_teste.shape}")
print("\n----------------------------------------------------")
print("Imagem em tons de cinza pela média das intensidades:")
print("----------------------------------------------------")
print(imagem_media)

print("\n------------------------------------------")
print("Imagem em tons de cinza pela fórmula NTSC:")
print("------------------------------------------")
print(imagem_nstc)