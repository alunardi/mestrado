from numpy import *
import string
import unicodedata

def removerCaracteresEspeciais(text) :
    safe_chars = string.ascii_letters + string.digits + '_'
    texto_limpo=''.join([char if char in safe_chars else ' ' for char in text])
    texto_limpo1 = texto_limpo.lower()
    return texto_limpo1

def recuperaOpiniao():
    from os import listdir
    f=open('hotel_72572.dat','r')
    words = f.read().split('<Author>')
    m = len(words)
    cont = 0
    for i in range(m-1):
        #posicao da opiniao
        review_inicial = ''
        review = ''
        texto = words[i+1].find('<Content>')
        texto = texto+9
        fim_texto = words[i+1].find('<Date>')
        fim_review = words[i+1].find('showReview')
        #posicao do rating
        rating = words[i+1].find('<Overall>')
        rating = rating+9
        fim_rating = words[i+1].find('<Value>')
        fim_rating = fim_rating - 1
        if fim_review<fim_texto and fim_review!=-1:
            review_inicial = words[i+1][texto:fim_review]
            review = removerCaracteresEspeciais(review_inicial)
            print review
        else:
            review_inicial = words[i+1][texto:fim_texto]
            review = removerCaracteresEspeciais(review_inicial)
            print review
        rating = words[i+1][rating:fim_rating]
        print rating
        final=open('Teste/%s/%s_%s.txt' %(rating, rating, cont),'a')
        final.write('%s\t' % (review))
        final.write('\n')
        cont = cont + 1
        f.close()