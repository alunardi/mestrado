from numpy import *
import string

def file2matrix():
    from os import listdir
    unigrama = {}
    for i in range(5):
        trainingFileList = listdir('Final/%s' % str(i+1))
        m = len(trainingFileList)
        review = [None]*m
        #print trainingFileList
        for j in range(m):
            fr = open('Final/%s/%s' % (str(i+1),trainingFileList[j]))
            review[j] = fr.read().split(" ")
            #conta as repeticoes dentro de uma frase quando esta comentado
            #review[j] = set(review[j])
            #review[j] = list(review[j])
            n = len(review[j])
            for k in range(n-1):
                unigrama[review[j][k]] = {}
                for z in range(5):
                    unigrama[review[j][k]][z] = 1
            fr.close()
    return unigrama

def file2matrixUni(unigrama):
    from os import listdir
    for i in range(5):
        trainingFileList = listdir('Final/%s' % str(i+1))
        m = len(trainingFileList)
        review = [None]*m
        for j in range(m):
            fr = open('Final/%s/%s' % (str(i+1),trainingFileList[j]))
            review[j] = fr.read().split(" ")
            #conta as repeticoes dentro de uma frase quando esta comentado
            #review[j] = set(review[j])
            #review[j] = list(review[j])
            n = len(review[j])
            for k in range(n-1):
                if i in unigrama[review[j][k]]:
                    unigrama[review[j][k]][i] += 1
            fr.close()
    return unigrama

def criaUnigramas():    
    token = file2matrix()
    unigrama = file2matrixUni(token)
    f=open('Unigramas/unigrama_total.txt','a')
    cont = 0
    for key in unigrama:
        soma = 0
        for j in range(5):
            soma = soma + unigrama[key][j]
        if soma>16:
            cont = cont+1
            f.write('%s\t' % (key))
            for j in range(5):
                f.write('%s\t' % unigrama[key][j])
            f.write('\n')
        unigrama.itervalues().next()
    f.close()
    print cont