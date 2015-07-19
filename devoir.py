#! /usr/bin/python
# -*- # -*- coding: utf-8 -*-
from package import tools_karkkainen_sanders

def algo_recherche_v1(texte,n, TS, mot):
    print "1.a) Algorithme élémentaire de recherche d'un mot ("+mot+") avec la table des suffixes."
    ga = 0
    dr = n
    while ga < dr :
        mil = (ga+dr)//2
        if mot > texte[TS[mil]:] :
            ga = mil + 1
        else:
            dr = mil
    deb = ga
    dr = n
    while ga < dr:
        mil = (ga+dr)//2
        if mot == texte[TS[mil]:][:len(mot)]:
            ga = mil+1
        else:
            dr = mil
    fin = dr
    res = range(deb,fin)
    print "Personnage = "+mot
    affichage(s, TS, HTR, res)
    return res

def algo_recherche_v2(texte, n, TS, HTR, mot):
    print "2.a"
    ga = 0
    dr = n
    while ga < dr :
        mil = (ga+dr)//2
        if mot > texte[TS[mil]:] :
            ga = mil + 1
        else:
            dr = mil
    deb = ga
    dr = n
    while ga < dr:
        mil = (ga+dr)//2
        if mot == texte[TS[mil]:][:len(mot)]:
            ga = mil+1
        else:
            dr = mil
    fin = dr
    return TS[deb:fin]

def plus_court_facteur_V1(s, TS, HTR):
    print "3.a) Algorithme de détection des plus courts facteurs uniques."
    res = []
    n = len(s)
    lgCandidat = [0]*(n+1)
    dat = [0]*(n+1)
    for i in xrange(0,n-1):
        lgCandidat[TS[i]] = 1 + max(HTR[i],HTR[i+1])
        dat[i] = 1 + max(HTR[i],HTR[i+1])
    lgCandidat[TS[n-1]] = 1 + HTR[n-1]
    lgCandidat[n] = 1
    i = 0
    while i+lgCandidat[i] <= n:
        if lgCandidat[i] <= lgCandidat[i+1] :
            res.append(s[i:i+lgCandidat[i]])
        i = i+1
    print "* Text = "+s
    print "i\tlgCandidat[i]\ttexte[i:i+lgCandidat[i]] "
    for i in xrange(0,len(lgCandidat)-1):
        print str(i)+"\t"+str(lgCandidat[i])+"\t"+"\t"+s[i:i+lgCandidat[i]]
    print "* Plus courts facteurs:"
    for pcf in res:
        print "\t"+pcf
    return res

def plus_court_facteur_V2(s, TS, HTR, k):
    print "3.b) Algorithme de détection des plus courts facteurs uniques qui ont une longueur supérieure à une valeur donnée ("+str(k)+")"
    res = []
    n = len(s)
    lgCandidat = [0]*(n+1)
    for i in xrange(0,n-1):
        lgCandidat[TS[i]] = 1 + max(HTR[i],HTR[i+1])
    lgCandidat[TS[n-1]] = 1 + HTR[n-1]
    lgCandidat[n] = 1
    i = 0
    while i+lgCandidat[i] <= n:
        if lgCandidat[i] <= lgCandidat[i+1] and lgCandidat[i] > k:
            res.append(s[i:i+lgCandidat[i]])
        i = i+1
    print "* Text = "+s
    print "i\tlgCandidat[i]\ttexte[i:i+lgCandidat[i]] "
    for i in xrange(0,len(lgCandidat)-1):
        print str(i)+"\t"+str(lgCandidat[i])+"\t"+"\t"+s[i:i+lgCandidat[i]]
    print "* Plus courts facteurs:"
    for pcf in res:
        print "\t"+pcf
    return res

def detection_supermaximales_V1(s, TS, HTR):
    print "4.a) Algorithme de détection des répétitions supermaximales"
    sm = []
    res = []
    d = -1
    #Etape 1
    for i in xrange(0,len(HTR)-1):
        if(HTR[i]<HTR[i+1]):
            d = i
        elif(HTR[i+1]<HTR[i] and d != -1):
            f = i
            sm.append((d,f));
            d = -1
    #Etape 2
    for sml in sm:
        leftChar = [s[x-1] for x in TS[sml[0]:sml[1]+1]]
        fSize = len(leftChar)
        sSize = len(list(set(leftChar)))
        if fSize == sSize:
            res+=[sml[0]+i for i in xrange(0,sml[1]-sml[0]+1)]
            print "\t"+s[TS[sml[1]]:TS[sml[1]]+HTR[sml[1]]]
    affichage(s, TS, HTR, res)
    return res

def detection_supermaximales_V2(s, TS, HTR, k):
    print "4.b) Algorithme de détection des répétitions supermaximales qui une longueur superérieure à une valeur donnée "+str(k)+"."
    sm = []
    d = -1
    #Etape 1
    for i in xrange(0,len(HTR)-1):
        if(HTR[i]<HTR[i+1]):
            d = i
        elif(HTR[i+1]<HTR[i] and d != -1 and HTR[i]>k):
            f = i
            sm.append((d,f));
            d = -1
    #Etape 2
    res = []
    for sml in sm:
        leftChar = [s[x-1] for x in TS[sml[0]:sml[1]+1]]
        fSize = len(leftChar)
        sSize = len(list(set(leftChar)))
        if fSize == sSize:
            res+=[sml[0]+i for i in xrange(0,sml[1]-sml[0]+1)]
            print "\t"+s[TS[sml[1]]:TS[sml[1]]+HTR[sml[1]]]
    affichage(s, TS, HTR, res)
    return res

def affichage(s, TS, HTR, res):
    print "* Text = "+s
    print "i\tTS\tHTR "
    for i in xrange(0,len(res)):
        print str(res[i])+"\t"+str(TS[res[i]])+"\t"+str(HTR[res[i]])+"\t"+s[TS[res[i]]:]

if __name__ == '__main__':
    s = "GATAAGATTGATG"
    #f = open('files/e-coli.txt', 'r')
    #s = f.read()
    TS = tools_karkkainen_sanders.direct_kark_sort(s)
    HTR = tools_karkkainen_sanders.LCP(s, TS)
    HTR.insert(0,0)
    del HTR[-1]
    mot = "ATG"
    Q1 = algo_recherche_v1(s,len(s), TS, mot)
    print ""
    Q3_a = plus_court_facteur_V1(s, TS , HTR)
    print ""
    Q3_b = plus_court_facteur_V2(s, TS , HTR, 2)
    print ""
    Q4_a = detection_supermaximales_V1(s, TS , HTR)
    print ""
    Q4_b = detection_supermaximales_V2(s, TS , HTR, 2)
