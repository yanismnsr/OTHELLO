from partie1 import *


def pion_adverse(joueur):
    """ Retourne l'entier correspondant à l'adversaire :
    - retourne 2 si joueur vaut 1,
    - retourne 1 si joueur vaut 2.
    Lève une erreur si joueur est différent de 1 et 2.
    """
    assert joueur == 1 or joueur == 2, "la valeur donnée en paramètre n'est pas valide"
    if joueur == 1:
        return 2
    return 1






def prise_possible_direction(p, i, j, vertical, horizontal, joueur):
    """ Retourne True si le joueur peut retourner un pion adverse
    dans la direction (vertical,horizontal) en posant un pion dans la case (i,j),
    False sinon.
    :Exemple:
    p = creer_plateau(4)
    prise_possible_direction(p,1,3,0,-1,2) retourne True
    prise_possible_direction(p,1,3,0,-1,1) retourne False
    prise_possible_direction(p,1,3,-1,-1,2) retourne False
    prise_possible_direction(p,1,0,0,1,1) retourne False
    """
    assert case_valide(p, i, j), "la case donnée n'est pas valide"
    assert joueur == 1 or joueur == 2, "le joueur n'est pas valide"
    if not case_valide(p, i+vertical, j+horizontal) or not get_case(p,i+vertical, j+horizontal) == pion_adverse(joueur) :
        return False
    i += vertical
    j += horizontal
    while case_valide(p, i, j) and get_case(p, i, j) == pion_adverse(joueur):
        i += vertical
        j += horizontal
    return case_valide(p,i,j) and get_case(p,i,j) == joueur







def mouvement_valide(plateau, i, j, joueur):
    """Retourne True si le joueur peut poser un pion à la case (i,j), False sinon.
    :Exemple:
    p = creer_plateau(4)
    mouvement_valide(p,1,3,2) # retourne True
    mouvement_valide(p,0,0,1) # retourne False
    """
    assert case_valide(plateau, i, j), "la case donnée n'est pas valide"
    assert joueur == 1 or joueur == 2, "le joueur n'est pas valide"
    tab=[
    [-1,-1],
    [-1,0],
    [-1,1],
    [0,-1],
    [0,1],
    [1,0],
    [1,1],
    [1,-1]
    ]
    for vertical, horizontal in tab:
        if get_case(plateau, i, j) == 0 and prise_possible_direction(plateau, i, j, vertical, horizontal, joueur):
            return True
    return False



def mouvement_direction(plateau, i, j, vertical, horizontal, joueur):
    """ Joue le pion du joueur à la case (i,j) si c'est possible.
    :Exemple:
    p = creer_plateau(4)
    mouvement_direction(p,0,3,-1,1,2) # ne modifie rien
    mouvement_direction(p,1,3,0,-1,2) # met la valeur 2 dans la case (1,2)
    """
    assert case_valide(plateau,i ,j), "la case n'est pas valide"
    assert joueur == 1 or joueur == 2, "le joueur n'est pas valide"
    if not prise_possible_direction(plateau, i, j, vertical, horizontal, joueur) :
        return False
    set_case(plateau, i, j, joueur)
    i += vertical
    j += horizontal
    while get_case(plateau, i, j) != joueur:
        set_case(plateau, i, j, joueur)
        i += vertical
        j += horizontal







def mouvement(plateau, i, j, joueur):
    """ Ajoute le pion du joueur à la case (i,j) et met à jour le plateau.

	:Exemple:

	p = creer_plateau(4)
	mouvement(p,0,3,2) # ne modifie rien
	mouvement(p,1,3,2) # met la valeur 2 dans les cases (1,2) et (1,3)
	"""
    if mouvement_valide(plateau, i, j, joueur):
        for vertical, horizontal in [[-1,-1],[-1,0],[1,-1],[0,1],[1,1],[1,0],[-1,1],[0,-1]]:
            if prise_possible_direction(plateau, i, j, vertical, horizontal, joueur):
                mouvement_direction(plateau, i, j, vertical, horizontal, joueur)
                



def joueur_peut_jouer(plateau, joueur):
    """ Retourne True s'il existe une case sur laquelle le joueur peut jouer,
    False sinon.
    :Exemple:
    p = creer_plateau(4)
    joueur_peut_jouer(p,1) # retourne True
    # On remplace les pions du joueur 2 par des pions du joueur 1
    set_case(p,1,1,1)
    set_case(p,2,2,1)
    joueur_peut_jouer(p,1) # retourne False
    """
    assert joueur == 1 or joueur == 2, "le joueur n'est pas valide"
    taille = plateau['n']
    for i in range(taille):
        for j in range(taille):
            if not get_case(plateau, i, j) and mouvement_valide(plateau, i, j, joueur):
                return True
    return False




def fin_de_partie(plateau):
    """ Retourne True si la partie est finie, 0 sinon.
    :Exemple:
    p = creer_plateau(4)
    fin_de_partie(p) # retourne False
    # On remplace les pions du joueur 2 par des pions du joueur 1
    set_case(p,1,1,1)
    set_case(p,2,2,1)
    fin_de_partie(p) # retourne True
    """
    if not joueur_peut_jouer(plateau, 1) and not joueur_peut_jouer(plateau, 2):
        return True
    return 0






def gagnant(plateau):
    """ Retourne :
    - 2 si le joueur 2 a plus de pions que le joueur 1,
    - 1 si le joueur 1 a plus de pions que le joueur 2,
    - 0 si égalité.
    :Exemple:
    p = creer_plateau(4)
    # On remplace les pions du joueur 2 par des pions du joueur 1
    set_case(p,1,1,1)
    set_case(p,2,2,1)
    gagnant(p) # retourne 1
    """
    dico_convertion = {0 : 0, 1 : 1, -1 : 2}
    score1 = plateau["cases"].count(1)
    score2 = plateau["cases"].count(2)
    return dico_convertion[(score1 > score2) - (score1 < score2)]








if __name__ == "__main__" :

    def test_pion_adverse():
        """
        cette fonction teste la fonction pion_adverse
        """
        assert pion_adverse(1) == 2
        assert pion_adverse(2) == 1

    test_pion_adverse()


    def test_prise_possible_direction():
        """
        cette fonction teste la fonction prise_possible_direction
        """
        p = creer_plateau(4)
        assert prise_possible_direction(p, 1, 3, 0, -1, 2)
        assert not prise_possible_direction(p, 1, 3, 0, -1, 1)
        assert not prise_possible_direction(p,1,3,-1,-1,2)
        assert prise_possible_direction(p,1,0,0,1,1)

    test_prise_possible_direction()


    def test_mouvement_valide():
        p = creer_plateau(4)
        assert mouvement_valide(p,1,3,2)
        assert not mouvement_valide(p,0,0,1)

    test_mouvement_valide()



    def test_mouvement_direction():
        p = creer_plateau(4)
        mouvement_direction(p,0,3,-1,1,2)
        assert get_case(p,1,1) == 2
        assert get_case(p,1,2) == 1
        assert get_case(p,2,1) == 1
        assert get_case(p,2,2) == 2
        mouvement_direction(p,1,3,0,-1,2)
        assert get_case(p,1,2) == 2

    test_mouvement_direction()


    def test_mouvement():
        p = creer_plateau(4)
        mouvement(p,0,3,2)
        assert get_case(p,1,1) == 2
        assert get_case(p,1,2) == 1
        assert get_case(p,2,1) == 1
        assert get_case(p,2,2) == 2
        mouvement(p,1,3,2)
        assert get_case(p,1,2) == 2
        assert get_case(p,1,3) == 2

    test_mouvement()


    def test_joueur_peut_jouer():
        p = creer_plateau(4)
        assert joueur_peut_jouer(p,1)
        set_case(p,1,1,1)
        set_case(p,2,2,1)
        assert not joueur_peut_jouer(p,1)

    test_joueur_peut_jouer()


    def test_fin_de_partie():
        p = creer_plateau(4)
        assert not fin_de_partie(p)
        set_case(p,1,1,1)
        set_case(p,2,2,1)
        assert fin_de_partie(p)

    test_fin_de_partie()


    def test_gagnant():
        p = creer_plateau(4)
        assert gagnant(p) == 0
        set_case(p,1,1,1)
        set_case(p,2,2,1)
        assert gagnant(p) == 1
        p = creer_plateau(4)
        set_case(p,1,2,2)
        set_case(p,2,1,2)
        assert gagnant(p) == 2

    test_gagnant()




    # test de la fonction pion adverse
    print("test de la fonction pion adverse")
    if pion_adverse(1) == 2 and pion_adverse(2) == 1 :
        print(True)
    else :
        print(False)


    # test de la fonction prise_possible_direction
    print("test de la fonction prise_possible_direction")

    p = creer_plateau(4)
    if prise_possible_direction(p,1,3,0,-1,2) and not prise_possible_direction(p,1,3,0,-1,1) and not prise_possible_direction(p,1,3,-1,-1,2) and prise_possible_direction(p,1,0,0,1,1) :
        print(True)
    else :
        print(False)

    afficher_plateau(p)

    print("teste de la fonction mouvement valide")
    print(mouvement_valide(p,1,3,2) and not mouvement_valide(p,0,0,1))


    print("test de la fonction mouvement_direction")
    mouvement_direction(p,0,3,-1,1,2)
    mouvement_direction(p,1,3,0,-1,2)

    p = creer_plateau(4)
    print("test de la fonction mouvement :")
    mouvement(p,0,3,2)
    mouvement(p,1,3,2)
    afficher_plateau(p)


    print("test de la fonction joueur_peut_jouer")
    p = creer_plateau(4)
    print(joueur_peut_jouer(p,1))
    set_case(p,1,1,1)
    set_case(p,2,2,1)
    print(joueur_peut_jouer(p,1))



    print("test de la fonction fin_de_partie")
    p = creer_plateau(4)
    print("le plateau est en son état initiale ")
    print(fin_de_partie(p))
    set_case(p,1,1,1)
    set_case(p,2,2,1)
    print("le plateau contient que des pions noirs ")
    print(fin_de_partie(p))



    print("test de la fonction gagnant")
    p = creer_plateau(4)
    set_case(p,1,1,1)
    set_case(p,2,2,1)
    afficher_plateau(p)
    print(gagnant(p))
