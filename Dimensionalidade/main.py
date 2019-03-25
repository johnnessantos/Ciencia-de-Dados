# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:32:01 2019

@author: johnn
"""
import timeseriesreduction as tsr
import matplotlib.pyplot as plt

#dados = np.random.random_sample(10)
dados = [0.01123527, 0.00515663, 0.16438734, 0.76631076, 0.58403357, 0.90953164, 
         0.58745028, 0.97205044, 0.79011735, 0.53830236]

listaAmostragem = tsr.amostragem(3,dados)
listaRandom = tsr.randomica(3,dados)
listaPAA = tsr.paa(4, dados)
listaSSV = tsr.ssv(4,dados)

plt.title("Redução de dimensinalidade")
original = plt.subplot(231)
original.set_title("Original")
original.axes.get_xaxis().set_visible(False)
original.axes.get_yaxis().set_visible(False)
original.plot(dados)

axrandom = plt.subplot(232)
axrandom.set_title("Random")
axrandom.axes.get_xaxis().set_visible(False)
axrandom.axes.get_yaxis().set_visible(False)
axrandom.plot(listaRandom)

axamostragem = plt.subplot(233)
axamostragem.set_title("Amostragem")
axamostragem.axes.get_xaxis().set_visible(False)
axamostragem.axes.get_yaxis().set_visible(False)
axamostragem.plot(listaAmostragem)

axpaa = plt.subplot(234)
axpaa.set_title("PAA")
axpaa.axes.get_xaxis().set_visible(False)
axpaa.axes.get_yaxis().set_visible(False)
axpaa.plot(listaPAA)

axssv = plt.subplot(235)
axssv.set_title("SSV")
axssv.axes.get_xaxis().set_visible(False)
axssv.axes.get_yaxis().set_visible(False)
axssv.plot(listaSSV)

plt.show()
