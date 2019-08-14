from numpy import *
import string

def trataNegacao():
    from os import listdir
    for i in range(5):
        trainingFileList = listdir('Total/%s' % str(i+1))
        m = len(trainingFileList)
        #print trainingFileList
        for j in range(m):
            fr = open('Total/%s/%s' % (str(i+1),trainingFileList[j]))
            review = fr.read()
            review = review.replace(" not ", " not_")
            review = review.replace(" no ", " no_")
            review = review.replace(" nothing ", " nothing_")
            print review
            grava=open('Final/%s/%s' % (str(i+1),trainingFileList[j]),'w')
            grava.write(review)
            grava.close()