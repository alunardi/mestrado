from numpy import *
import string
#inicia os vetores
def file2matrix():
    from os import listdir
    ngrama = {}
    for i in range(5):
        trainingFileList = listdir('Final/%s' % str(i+1))
        m = len(trainingFileList)
        review = [None]*m
        #print trainingFileList
        for j in range(m):
            fr = open('Final/%s/%s' % (str(i+1),trainingFileList[j]))
            review[j] = fr.readline().split(" ")
            #conta as repeticoes dentro de uma frase quando esta comentado
            review[j] = set(review[j])
            review[j] = list(review[j])
            n = len(review[j])
            for k in range(n):
                aux = review[j][k]
                if k>0 and k<n-2:
                        expressao = aux + "_" + review[j][k+1]
                        ngrama[expressao] = {}
                        for z in range(5):
                            ngrama[expressao][z] = 1
            fr.close()
    return ngrama
#preenche os vetores
def file2matrixN(ngrama):
    from os import listdir
    for i in range(5):
        trainingFileList = listdir('Final/%s' % str(i+1))
        m = len(trainingFileList)
        review = [None]*m
        for j in range(m):
            fr = open('Final/%s/%s' % (str(i+1),trainingFileList[j]))
            review[j] = fr.readline().split(" ")
            #conta as repeticoes dentro de uma frase quando esta comentado
            review[j] = set(review[j])
            review[j] = list(review[j])
            n = len(review[j])
            for k in range(n):
                aux = review[j][k]
                if k>0 and k<n-2:
                        expressao = aux + "_" + review[j][k+1]
                        if i in ngrama[expressao]:
                            ngrama[expressao][i] += 1
            fr.close()
    return ngrama

def criaNGramas():    
    token = file2matrix()
    ngrama = file2matrixN(token)
    f=open('Bigramas/ngrama_sem_repeticao.txt','a')
    cont = 0
    for key in ngrama:
        soma = 0
        for j in range(5):
            soma = soma + ngrama[key][j]
        if soma>16:
            cont = cont+1
            f.write('%s\t' % (key))
            for j in range(5):
                f.write('%s\t' % ngrama[key][j])
            f.write('\n')
        ngrama.itervalues().next()
    f.close()
    print cont