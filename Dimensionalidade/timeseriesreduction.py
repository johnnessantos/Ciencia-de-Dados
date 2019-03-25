# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:32:01 2019

@author: johnn
"""
import random as rd
import math

# A técnica Random consiste em enumerar o conjunto de dados
# original e selecionar os dados que farão parte do conjunto de
# dados final de forma aleatória, mantendo a sua ordem.
def randomica(n, dados):
    lista = []
    retorno = []
    for i in range(n):
        lista.append(rd.randint(0,len(dados)-1))
    lista.sort()
    print(lista)
    for i in lista:
        retorno.append(dados[i])
    return retorno

# Este metodo retorna os dados multiplos de k
def amostragem(k, dados):
    indice = 0
    lista = []
    while(indice < len(dados)):
        lista.append(dados[indice])
        indice += k
        
    return lista

# Este metodo consiste em dividir a lista de pontos em segmentos de tamanho k
# e realizar a média para cada cluster representando assim um ponto.
def paa(k, pontos):
    tam = len(pontos)
    
    if tam < k:
        return pontos

    lista = []
    while(len(lista) < tam/k):
        index = len(lista)*k
        lista.append(sum(pontos[index:index+k]))
    return lista

# Este metodos consiste me dividir os dados em segmentos de tamanho k, onde o segmento
# Si+1 e formado pelo ultimo elemento do segmento Si, representando a conectividade entre 
# os segmentos
def ssv(k, pontos):
    tam = len(pontos)
    
    if tam < k or k == 1:
        return pontos

    lista = []
    quantidadePontos = int(int(tam + (tam/k))/k)
    while(len(lista) < quantidadePontos):
        index = 0 if len(lista) == 0 else len(lista)*k-1
        soma = 0
        for i in range(k-1):
            if(index+i < tam-1):
                soma += abs(pontos[index+i] - pontos[index+i+1])
        lista.append(soma)
    return lista


def diferencaEntrePontos(x1,y1,x2,y2):
    if(y1-y2)== 0:
        return 0
    return float((math.sqrt(x1-x2)**2)/((y1-y2)**2))

def pip(n, pontos):
    lista = []
    return lista
