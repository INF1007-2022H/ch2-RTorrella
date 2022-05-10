#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    for lettre in mot:
        x= " "
        if ord(lettre)>=65 and ord(lettre)<=90:
            x=ord(lettre) + 32
    return "Cette lettre en minuscule est " + chr(x)

def minuscule(mot):
    for lettre in mot:
        x= " "
        if ord(lettre)>=97 and ord(lettre)<=122:
            x=ord(lettre) - 32
    return "Cette lettre en majuscule est " + chr(x)


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
