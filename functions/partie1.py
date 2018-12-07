#j'ai eu quelques difficultés à telecharger la bibliothèque termcolor, 
# en conséquence, j'ai directement telechargé le module et je l'ai placé 
# dans le meme repertoire que ce fichier
import sys
sys.path.append("./termcolor-master")
from termcolor import *


def indice_valide(plateau, indice):
    """ Retourne True si indice est un indice valide de case pour le plateau
    (entre 0 et n-1)
    :Exemple:
    p = creer_plateau(8)
        indice_valide(p,0)
    # retourne True
    indice_valide(p, 18) # retourne False
    """
    lim = plateau["n"]
    if indice < lim :
        return True
    return False




def case_valide(plateau, i, j) :
    """ Retourne True si (i,j) est une case du plateau (i et j sont des indices
    valides)
    :Exemple:
    p = creer_plateau(8)
    case_valide(p,3,3) # retourne True
    case_valide(p,18,3) # retourne False
    """
    if indice_valide(plateau,i) and indice_valide(plateau, j):
        return True 
    return False



def get_case(plateau, i, j):
    """ Retourne la valeur de la case (i,j). Erreur si (i,j) n'est pas valide.
    :Exemple:
    p = creer_plateau(4)
    get_case(p,0,0) # retourne 0 (la case est vide)
    get_case(p,1,1) # retourne 2 (la case contient un pion blanc)
    get_case(p,1,2) # retourne 1 (la case contient un pion noir)
    get_case(p,18,3) # lève une erreur
    """
    assert case_valide(plateau, i, j), "l'indice n'est pas valide"
    tab = plateau["cases"]
    taille = plateau["n"]
    return tab[i*taille+j]




def set_case(plateau, i, j, val):
    """ Affecte la valeur val dans la case (i,j). Erreur si (i,j) n'est pas une case
    ou si val n'est pas entre 0 et 2.
    Met aussi à jour le nombre de cases libres (sans pion).
    :Exemple:
    p = creer_plateau(4)
    set_case(p,0,0,1) # met un pion noir (i.e., met la valeur 1) dans la case (0,0)
    set_case(p,1,2,0) # enlève le pion (i.e., met la valeur 0) dans la case (1,2)
    set_case(p,18,3,1) # lève une erreur
    set_case(p,2,3,6) # lève une erreur
    """
    assert case_valide(plateau, i, j), "l'indice n'est pas valide"
    tab = plateau["cases"]
    taille = plateau["n"]
    tab[i*taille+j] = val




def creer_plateau(n):
    """Retourne une nouvelle partie. Lève une erreur si n est différent de 4, 6 ou 8.
    Une partie est un dictionnaire contenant :
    - n : valeur passée en paramètre
    - cases : tableau de n*n cases initialisées
    :Exemple:
    creer_plateau(4) retourne un dictionnaire contenant les entrées (couples clés/val
    - n : 4
    - cases : [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]
    """
    assert n == 4 or n == 6 or n == 8, "la valeure donnée n'est pas une taille de plateau possible"
    plateau = {}
    plateau["n"] = n
    plateau["cases"] = []
    tab = plateau["cases"]
    taille = n*n
    i = 0
    for i in range(taille):
        tab.append(0)
        i += 1
    i = n//2 - 1
    j = n//2 - 1
    set_case(plateau, i, j, 2)
    set_case(plateau, i, j+1, 1)
    i = n//2
    j = n//2 - 1
    set_case(plateau, i, j, 1)
    set_case(plateau, i, j+1, 2)
    return plateau


def int_convert(n):
    """cette fonction prend un entier en paramètre et renvoie la lettre 
    correspondante de façon à ce que ce soit adapté à la ligne verticale 
    l'affichage"""
    if n == 0 :
        return 'a'
    if n == 1 :
        return 'b'
    if n == 2 :
        return 'c'
    if n == 3 :
        return 'd'
    if n == 4 :
        return 'e'
    if n == 5 :
        return 'f'
    if n == 6 :
        return 'g'
    if n == 7 :
        return 'h'



def afficher_plateau(plateau):
    """Affiche le plateau à l'écran. """
    taille = plateau["n"]
    tab = plateau["cases"]
    assert taille == 4 or taille == 6 or taille == 8, "l'indice n'est pas valide"
    chaine = '   '
    for i in range(taille) :
        chaineConcat = '   ' + str(i+1) + '   '
        chaine += chaineConcat
    print(chaine)

    # premiere boucle qui parcourt les lignes 
    for i in range(taille):

        # cette boucle fait 3 fois la succession des couleurs afin d'avoir 
        # un bon affichage 
        for j in range(3):
            if j%2 == 0 :
                chaine = '   '
            else :
                chaine = ' ' + int_convert(i) + ' '
            # cette boucle parcourt les colonnes
            for k in range(taille):
                # si la ligne est pair alors on commence avec le magenta
                if i%2 == 0 :
                    if k%2 == 0:
                        if j%2 == 0 :
                            chaine += colored('       ', None, 'on_magenta')
                        else :
                            if get_case(plateau, i, k) == 1 :
                                chaine += colored('  ###  ' , 'grey', 'on_magenta')
                            elif get_case(plateau, i, k) == 0 :
                                chaine += colored('       ', None, 'on_magenta')
                            else :
                                chaine += colored('  ###  ', None, 'on_magenta')
                    else :
                        if j%2 == 0:
                            chaine += colored('       ', None, 'on_blue')
                        else :
                            if get_case(plateau, i, k) == 1:
                                chaine += colored('  ###  ' , 'grey', 'on_blue')
                            elif get_case(plateau, i, k) == 0 :
                                chaine += colored('       ', None, 'on_blue')
                            else :
                                chaine += colored('  ###  ', 'white', 'on_blue')
                
                # si la ligne est impair alors on commence par le bleu 
                else:
                    if k%2 == 0 :
                        if j%2 == 0:
                            chaine += colored('       ', None, 'on_blue')
                        else :
                            if get_case(plateau, i, k) == 1:
                                chaine += colored('  ###  ' , 'grey', 'on_blue')
                            elif get_case(plateau, i, k) == 0 :
                                chaine += colored('       ', None, 'on_blue')
                            else :
                                chaine += colored('  ###  ', 'white', 'on_blue')
                    else :
                        if j%2 == 0 :
                            chaine += colored('       ', None, 'on_magenta')
                        else :
                            if get_case(plateau, i, k) == 1 :
                                chaine += colored('  ###  ' , 'grey', 'on_magenta')
                            elif get_case(plateau, i, k) == 0 :
                                chaine += colored('       ', None, 'on_magenta')
                            else :
                                chaine += colored('  ###  ', None, 'on_magenta')
            print(chaine)
            
            



if __name__ == "__main__" :
    dico = creer_plateau(8)
    afficher_plateau(dico)


    #test de la fonction indice valide 
    print('test de la fonction indice_valide')
    dico = creer_plateau(4)
    if indice_valide(dico, 1) and not indice_valide(dico, 4) :
        print(True)
    else :
        print(False)




    #test de la fonction case valide 
    print('test de la fonction case_valide')
    dico = creer_plateau(4)
    if case_valide(dico, 3, 3) and not case_valide(dico, 4,5):
        print (True)
    else :
        print(False)




    #test de la fonction get_case
    print('test de la fonction get_case')
    if get_case(dico, 1,1) == 2 and get_case(dico, 1, 2) == 1 :
        print(True)
    else :
        print(False)



    # test de la fonction set_case
    print('test de la fonction set_case')
    set_case(dico, 0, 0, 1)
    if get_case(dico, 0, 0) == 1 :
        print(True)
    else :
        print(False)
    
    afficher_plateau(dico)


    # la fonction creer_plateau fonctionne bien puisqu'on l'a utilisé en premier
    # et le reste des fonctions fonctionnent correctement 

