#!/usr/bin/python
# -*- coding: utf-8 -*-

def testa_primo(n):
    teste=1
    for i in range(2,n):
        if n % i == 0:
            teste=teste+1
    if teste != 1:
        print('Número não primo')
    else:
        print ('Número primo')