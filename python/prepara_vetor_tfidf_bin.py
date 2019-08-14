from numpy import *
import string

def file2matrix(filename):
    fr = open(filename)
    log = fr.read().split("\n")
    fr.close()
    return log

def file2corpus(filename):
    fr = open(filename)
    log = fr.read()
    log_2 = string.ascii_letters + string.digits
    log_final =''.join([char if char in log_2 else '' for char in log])
    fr.close()
    return log

def buscaArquivos(dirName,m,num):
    from os import listdir
    hwLabels = []
    trainingFileList = listdir(dirName)           #load the training set
    #m = len(trainingFileList)
    k = m-500
    corpus = [None]*500
    for i in range(m):
        if i >= k:
            fileNameStr = trainingFileList[i]
            fileStr = fileNameStr.split('.')[0]     #take off .txt
            classNumStr = int(fileStr.split('_')[0])
            if classNumStr == 1 or classNumStr == 2 or classNumStr == 3:
                hwLabels.append(1)
            elif classNumStr == 4 or classNumStr == 5:
                hwLabels.append(2)
            else: hwLabels.append(-1)
            z = i-k            
            corpus[z] = file2corpus('%s/%s' % (dirName, fileNameStr))	    
    token = file2matrix('Bigramas/chi_%s_bi.txt' % num)
    return corpus, hwLabels, token

def addVetorTXT(vetor,label, num):
    f=open('Bigramas/%s_chi_bi_tfidf_123_45.arff' % num,'a')
    for i in range(len(vetor)):
        for j in range(len(vetor[i])):
            f.write(str(vetor[i][j])+',')
        f.write(str(label[i])+'\n')
    f.close()

def Vectorizer(num):
	from sklearn.feature_extraction.text import CountVectorizer
	vectorizer = CountVectorizer(min_df=1)
	f=open('Bigramas/%s_chi_bi_tfidf_123_45.arff' % num,'a')
	f.write('@RELATION texto\n\n')
	for i in range(num-1):
		f.write('@ATTRIBUTE\t'+str((i+1))+'\tREAL\n')
	f.write('@ATTRIBUTE\tclass\t{1, 2}\n\n@DATA\n')
	f.close()
	for i in range(3):
		for j in range(5):
			corpus,labels,token = buscaArquivos('Final/%s' % (j+1),(i+1)*500,num)
			#from sklearn.feature_extraction.text import HashingVectorizer
			#hv = HashingVectorizer(n_features=500)
			#Z = hv.transform(corpus)
			#addVetorTXT(Z.toarray(),labels)
			vectorizer.fit_transform(token)
			X = vectorizer.transform(corpus)
			from sklearn.feature_extraction.text import TfidfTransformer
			transformer = TfidfTransformer()
			Y = transformer.fit_transform(X.toarray())			
			addVetorTXT(Y.toarray(),labels, num)