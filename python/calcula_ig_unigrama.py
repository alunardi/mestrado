from numpy import *
import string
import math

def file2matrix(filename):
    fr = open(filename)
    log = fr.read().split("\n")
    #print log
    fr.close()
    return log

def buscaUnigrama(filename):
    unigrama_linha = file2matrix(filename)
    unigrama = {}
    m = len(unigrama_linha)
    for i in range(m):
        vetor_aux = unigrama_linha[i]
        vetor = vetor_aux.split('\t')
        word = vetor[0]
        z = len(vetor)
        unigrama[word] = {}
        soma = 0
        for j in range(z-2):
            unigrama[word][j] = vetor[j+1]
            soma = soma + int(vetor[j+1])
        unigrama[word][z-2] = soma
    return unigrama

def salvaArquivo(filename, num, unigrama):
    f=open(filename,'a')
    for i in range(num):
        print unigrama[i][0]
        f.write('%s\n' % (unigrama[i][0]))
    f.close()

def calculaIg(num):
    unigrama_total = buscaUnigrama('Unigramas/unigrama_sem_repeticao.txt')
    total_review = [1500.0,1500.0,1500.0,1500.0,1500.0]
    numero_review = 7500.0
    import numpy as np
    #unigrama_sem_repeticao = buscaUnigrama('unigrama_sem_repeticao.txt')
    #ver letras correspondentes no artigo - dissertacao
    ig = {}
    ig_final = {}
    for key in unigrama_total:
        #print key
        ig[key] = [None]*5
        if key != '':
            ganho = 0.0
            entropia_classe = 0.0
            entropia_termo = 0.0
            entropia_nao_termo = 0.0
            for j in range(5):
                #calculo do ganho de informacao de acordo com Tan and Zhang
                review = float(total_review[j])
                entropia_classe = entropia_classe + (review/numero_review*(np.math.log(review/numero_review, 2)))
                termo_classe = float(unigrama_total[key][j])
                termo_nao_classe = review - termo_classe
                valor1 = np.math.log(termo_classe/review, 2)
                entropia_termo = entropia_termo + (termo_classe/review*(valor1))
                valor2 = np.math.log(termo_nao_classe/review, 2)
                entropia_nao_termo = entropia_nao_termo + (termo_nao_classe/review*(valor2))                
            ganho  = -entropia_classe + entropia_termo + entropia_nao_termo
            if ganho < 0.0:
                ganho = ganho*(-1)
            ig_final[key] = ganho
    import operator
    sorted_x = sorted(ig_final.items(), key=operator.itemgetter(1), reverse=False)
    salvaArquivo('Unigramas/ig_%s_uni.txt' % num,num,sorted_x)