#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    x= " "
    if ord(x)>=65 and ord(x)<=90:
    x=ord(x) + 32
    return "Cette lettre en minuscule est " + chr(x)
def minuscule(mot):
    x= " "
    if ord(x)>=97 and ord(x)<=122:
    x=ord(x) - 32
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
