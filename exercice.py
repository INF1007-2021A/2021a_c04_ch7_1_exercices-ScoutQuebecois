#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici

from turtle import Turtle


# TODO: Définissez vos fonction ici

def recur_tree(tur,i):
    
    if (i>10):
        tur.fd(i)
        tur.left(i/2)
        recur_tree(tur,2/3 * i)
        tur.right(i)
        recur_tree(tur,2/3 * i)
        tur.left(i/2)
        tur.bk(i)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    tur = Turtle()
    tur.left(90)
    recur_tree(tur,100)
    pass
