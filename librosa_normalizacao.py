from scipy.ndimage import interpolation
import librosa
import numpy as np
import os

#PATH = 'dataset-numeros-falados/gravacoes/'
PATH = 'gravacoes/'
N_INPUT = 3000

for root, dirs, files in os.walk(PATH):
    for filename in files:
        print(filename)

        filename_input = PATH + filename
        vetor, sr = librosa.load(filename_input, sr=None, mono=True, duration=1)

        print(vetor.shape)

        tam = len(vetor)
        redin = 1 - ((tam - N_INPUT)/tam)
        save = interpolation.zoom(vetor, redin)

        print(save.shape)

        file_save = 'audio_saida/' + filename
        librosa.output.write_wav(file_save, save, sr)
