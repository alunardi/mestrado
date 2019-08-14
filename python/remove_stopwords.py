from numpy import *
import string

def retiraStopwords():
    from os import listdir
    for i in range(5):
        trainingFileList = listdir('Total/%s' % str(i+1))
        m = len(trainingFileList)
        #print trainingFileList
        for j in range(m):
            fr = open('Total/%s/%s' % (str(i+1),trainingFileList[j]))
            review = fr.read()
            print review
            stop=open('stopwords.txt','r')
            stopwords = stop.read().split('\n')
            stop.close()
            n = len(stopwords)
            for k in range(n-1):
                review = review.replace(" %s " % stopwords[k], " ")
                review = review.replace("\n"," ")
            print review
            grava=open('Total/%s/%s' % (str(i+1),trainingFileList[j]),'w')
            grava.write(review)
            grava.close()