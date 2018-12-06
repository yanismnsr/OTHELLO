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
    while i < taille:
        tab.append[0]
        i += 1
    i = n/2 - 1
    j = n/2 - 1
    tab[i*taille + j] = 2
    tab[i*taille + j + 1] = 1
    i = n/2
    j = n/2 - 1
    tab[i*taille + j] = 1
    tab[i*taille + j + 1] = 2
    return plateau






if __name__ == "__main__" :
    dico = creer_plateau(8)
    print (dico["cases"])
