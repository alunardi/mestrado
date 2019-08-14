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

def buscaNgrama(filename):
    ngrama_linha = file2matrix(filename)
    ngrama = {}
    m = len(ngrama_linha)
    for i in range(m):
        vetor_aux = ngrama_linha[i]
        vetor = vetor_aux.split('\t')
        word = vetor[0]
        z = len(vetor)
        ngrama[word] = {}
        soma = 0
        for j in range(z-2):
            ngrama[word][j] = vetor[j+1]
            soma = soma + int(vetor[j+1])
        ngrama[word][z-2] = soma
    return ngrama

def salvaArquivo(filename, num, unigrama):
    f=open(filename,'a')
    for i in range(num):
        print unigrama[i][0]
        f.write('%s\n' % (unigrama[i][0]))
    f.close()

def calculaChi(num):
    ngrama_total = buscaNgrama('Bigramas/ngrama_total.txt')
    unigrama_total = buscaUnigrama('Unigramas/unigrama_total.txt')
    ngrama_total.update(unigrama_total)
    #print ngrama_total
    total_review = [1500,1500,1500,1500,1500]
    #unigrama_sem_repeticao = buscaUnigrama('unigrama_sem_repeticao.txt')
    #ver letras correspondentes no artigo - dissertacao
    chi = {}
    chi_final = {}
    for key in ngrama_total:
        #print key
        chi[key] = [None]*5
        if key != '':
            for j in range(5):
                n = 7500
                a = float(ngrama_total[key][j])                
                b = float(ngrama_total[key][5]) - a
                e = total_review[j] - a                
                d = n - (total_review[j] + float(ngrama_total[key][5]) - a)
                valor1 = n*(pow((a*d)-(b*e),2))
                valor2 = ((a+e)*(b+d)*(a+b)*(e+d))
                valor3 = round(valor1/valor2,5)
                chi[key][j] = valor3
            chi_final[key] = max(chi[key])
    import operator
    sorted_x = sorted(chi_final.items(), key=operator.itemgetter(1), reverse=True)
    salvaArquivo('Bigramas/chi_%s_bi.txt' % num,num,sorted_x)