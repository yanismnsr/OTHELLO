#j'ai eu quelques difficultés à telecharger la bibliothèque termcolor,
# en conséquence, j'ai directement telechargé le module et je l'ai placé
# dans le meme repertoire que ce fichier
from termcolor import *
#import sys
#sys.path.append("./termcolor-master")
#from termcolor import *


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
    return 0 <= indice < lim




def case_valide(plateau, i, j) :
    """ Retourne True si (i,j) est une case du plateau (i et j sont des indices
    valides)
    :Exemple:
    p = creer_plateau(8)
    case_valide(p,3,3) # retourne True
    case_valide(p,18,3) # retourne False
    """
    return indice_valide(plateau,i) and indice_valide(plateau, j)



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
    assert 0 <= val <= 2 , "la valeure indiquée n'est pas entre 0 et 2"
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
    taille = n*n
    plateau["cases"] = [0] * taille
    tab = plateau["cases"]

    i = n//2 - 1
    j = n//2 - 1
    set_case(plateau, i, j, 2)
    set_case(plateau, i, j+1, 1)
    i = n//2
    j = n//2 - 1
    set_case(plateau, i, j, 1)
    set_case(plateau, i, j+1, 2)
    return plateau





def on_color(i, j):
    """
    fonction qui permet de définir la couleur du font en fonction de
    la parité de la case
    """
    if i%2 == j%2:
        return 'on_magenta'
    else :
        return 'on_cyan'




def get_pion(plateau , i, j):
    """
    fonction qui retourne la chaine de caractère a mettre dans chaque case
    en fonction du numéro du joueur
    """
    onColor = on_color(i, j)
    taille = plateau['n']
    tab = plateau['cases']
    if get_case(plateau, i, j) == 1:
        return colored('  ###  ', 'grey', onColor, attrs=['dark'])
    elif get_case(plateau, i, j) == 2 :
        return colored("  ###  ", None, onColor)
    else :
        return colored(' ' * 7, None , onColor)


def get_chaine_init(indice_sous_ligne, indice_ligne):
    """
    retourne le caractère à mettre au debut de chaque ligne en fonction
    de la ligne et la sous_ligne
    La sous_ligne prend les valeurs 0, 1 ou 2 ; car chaque ligne est composée
    de 3 sous_lignes
    """
    # dictionnaire qui permet de determiner la lettre correspondante au numéro
    # de la ligne
    dico_lettres = {0 : 'a', 1 : 'b' , 2 : 'c' , 3 : 'd' , 4 : 'e' , 5 : 'f' , 6 : 'g' , 7 : 'h'}
    if indice_sous_ligne%2 == 0:
        return ' ' * 3
    else :
        return ' ' + dico_lettres[indice_ligne] +' '



def afficher_plateau (plateau):
    """
    fait l'affichage du plateau
    """
    taille = plateau["n"]
    assert taille == 4 or taille == 6 or taille == 8, "l'indice n'est pas valide"
    tab = plateau["cases"]
    ligne = ' ' * 3

    # boucle qui affiche la premiere ligne des numéros de colonne
    for i in range(taille) :
        ligne += ' ' * 3 + str(i+1) + ' ' * 3
    print(ligne)

    # boucle qui parcourt les lignes
    for i in range(taille):
        # boucle qui parcourt 3 fois chaque ligne (une ligne est composée de 3
        # sous-lignes)
        for j in range(3):
            ligne = get_chaine_init(j, i)      # initialisation de la sous-ligne
            # boucle qui parcourt les colonnes
            for k in range(taille):
                if j%2 == 0:
                    ligne += colored(' ' * 7, None, on_color(i, k))
                else :
                    ligne += get_pion(plateau, i, k)
            print(ligne)








if __name__ == "__main__" :
    dico = creer_plateau(8)
    print("test de la fonction afficher_plateau")
    afficher_plateau(dico)


    print("")


    #test de la fonction indice valide
    print('test de la fonction indice_valide')
    dico = creer_plateau(4)
    if indice_valide(dico, 1) and not indice_valide(dico, 4) :
        print(True)
    else :
        print(False)


    print("")

    #test de la fonction case valide
    print('test de la fonction case_valide')
    dico = creer_plateau(4)
    if case_valide(dico, 3, 3) and not case_valide(dico, 4,5):
        print (True)
    else :
        print(False)


    print("")


    #test de la fonction get_case
    print('test de la fonction get_case')
    if get_case(dico, 1,1) == 2 and get_case(dico, 1, 2) == 1 :
        print(True)
    else :
        print(False)

    print("")

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
