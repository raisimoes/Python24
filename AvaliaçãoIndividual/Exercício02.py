import numpy as np

def rgb2gray(imagem_rgb, conversion_method='ntsc'):
    if not isinstance(imagem_rgb, np.ndarray) or imagem_rgb.shape[-1] != 3:
        raise ValueError("O argumento de entrada deve ser uma imagem RGB representada por um ndarray 3D.")

    if conversion_method.lower() not in ['media', 'ntsc']:
        raise ValueError("O método de conversão deve ser 'media' ou 'ntsc'.")

    if conversion_method.lower() == 'media':
        imagem_tons_cinza = np.mean(imagem_rgb, axis=-1)
    else:  # Método NTSC
        weights = np.array([0.2989, 0.5870, 0.1140])
        imagem_tons_cinza = np.dot(imagem_rgb, weights)

    imagem_tons_cinza = np.clip(imagem_tons_cinza, 0, 255)

    imagem_tons_cinza = imagem_tons_cinza.astype(np.uint8)

    return imagem_tons_cinza

imagem_rgb = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8) 