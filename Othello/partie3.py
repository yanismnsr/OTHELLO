from partie2 import *
from os import system
from json import *
import os
import sys

def creer_partie(n):
    """ Crée une partie. Une partie est un dictionnaire contenant :
    - le joueur dont c'est le tour (clé joueur) initialisé à 1,
    - le plateau (clé plateau).
    :Exemple:
    creer_partie(4) retourne un dictionnaire contenant les entrées
    (couples clés/valeurs) :
    - joueur : 1
    - plateau : {
    - n : 4,
    - cases : [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]
    }
    """
    assert n == 4 or n == 6 or n == 8, "la taille n'est pas valide"
    p = creer_plateau(n)
    partie = {
    "joueur" : 1,
    "plateau" : p
    }
    return partie


#fonction en plus
def letter_lim (partie) :
    """
    cette fonction retourne la lettre limite d'un plateau
    Retourne d si le plateau est de taille 4
    Retourne f si le plateau est de taille 6
    retourne h si le plateau est de taille 8
    """
    dico = {
    4 : "d",
    6 : "f",
    8 : "h"
    }
    taille = partie["plateau"]["n"]
    return dico[taille]




def saisie_valide(partie, s):
    """ Retourne True si la chaîne s correspond à un mouvement valide pour le joueur
    et False sinon.
    La chaîne s est valide si :
    - s est égal à la lettre M ou
    - s correspond à une case (de la forme a1 pour la case (0,0), ..., h8 pour la cas
    où le joueur courant peut poser son pion.
    :Exemple:
    p = creer_partie(4)
    saisie_valide(p, "M") # retourne True
    saisie_valide(p, "b1") # retourne True
    saisie_valide(p, "b4") # return False
    """
    if s == "M" :
        return True
    if len(s) > 2:
        return False
    try:
        ligne = ord(s[0]) - ord("a")
        colonne = int(s[1]) - 1
    except:
        return False
    return mouvement_valide(partie["plateau"], ligne , colonne, partie["joueur"])


def effacer_terminal():
    """ Efface le terminal. """
    system('clear') #pour linux


#fonction en plus
def saisie_controle(partie) :
    joueur = partie["joueur"]
    print("joueur", joueur)
    print("saisissez un mouvement ou M pour revenir au menu principale :")
    saisie = input()
    while not saisie_valide(partie, saisie) :
        print("joueur" , joueur)
        print("saisissez un mouvement ou M pour revenir au menu principale :")
        saisie = input()
    return saisie


#fonction en plus
def chaine2num(chaine):
    """
    cette fonction convertit une chaine ce caractère désignant un
    mouvement en un tableau de longueur 2 qui comporte la ligne
    à la première case et la colonne à la 2ème case
    """
    assert len(chaine) == 2, "la longueur de la chaine est différente de 2"
    tab = [ord(chaine[0]) - ord("a"), int(chaine[1])-1]
    return tab



def tour_jeu(partie):
    """ Effectue un tour de jeu :
    - efface le terminal,
    - affiche le plateau,
    - si le joueur courant peut jouer, effectue la saisie d'un mouvement valide
    (saisie contrôlée),
    - Effectue le mouvement sur le plateau de jeu,
    - Retourne True si le joueur courant a joué ou False s'il souhaite accéder
    au menu principal.
    :Exemple:
    p = creer_partie(4)
    tour_jeu(p)
    #Si l'utilisateur a saisi b1, alors p vaut :
    {
    "joueur" : 1,
    "plateau" : {
    "n" : 4,
    "cases" : [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]
    }
    }
    """
    saisie = saisie_controle(partie)
    if len(saisie) == 2:
        tab_mouv = chaine2num(saisie)
        i = tab_mouv[0]
        j = tab_mouv[1]
        mouvement(partie["plateau"], i, j, partie["joueur"])
        effacer_terminal()
        afficher_plateau(partie["plateau"])
        return True
    else :
        return False



def saisir_action(partie):
    """ Retourne le choix du joueur pour menu (saisie contrôlée):
    - 0 pour terminer le jeu,
    - 1 pour commencer une nouvelle partie,
    - 2 pour charger une partie,
    - 3 pour sauvegarder une partie (si une partie est en cours),
    - 4 pour reprendre la partie (si une partie est en cours).
    :Exemple:
    n = saisir_action(None)
    n est un entier compris entre 0 et 2 inclus.
    """
    opt1 = " Menu \n- 0 pour terminer le jeu, \n- 1 pour commencer une nouvelle partie, \n- 2 pour charger une partie."
    opt2 = " Menu \n- 0 pour terminer le jeu, \n- 1 pour commencer une nouvelle partie, \n- 2 pour charger une partie, \n- 3 pour sauvegarder une partie, \n- 4 pour reprendre la partie."
    if partie is None:
        print(opt1)
        s = int(input())
        while not 0 <= s <= 2:
            print(opt1)
            s = int(input())
    else:
        print(opt2)
        s = int(input())
        while not 0 <= s <= 4:
            print(opt2)
            s = int(input())
    return s


#fonction en plus
def menu (partie, action):
    """
    cette fonction effectue l'action retournée par la fonction saisir_action
    """
    assert 0 <= action <= 4, "l'action n'est pas valide"
    if action == 0:
        exit()
    elif action == 1:
        taille = saisir_taille_plateau()
        return creer_partie(taille)
    elif action == 2:
        return charger_partie()
    elif action == 3:
        sauvegarder_partie(partie)
        return partie
    return partie


def jouer(partie) :
    """ Permet de jouer à la partie en cours (passée en paramètre).
    Retourne True si la partie est terminée, False sinon.
    :Exemple:
    p = creer_partie(4)
    res = jouer(p)
    Si res vaut True, alors les deux joueurs ont fait une partie entière d'Othello
    sur une grille 4 * 4.
    """
    while not fin_de_partie(partie["plateau"]):
        if joueur_peut_jouer(partie["plateau"],partie["joueur"]):
            played = tour_jeu(partie)
            if not played:
                return False
        partie["joueur"] = pion_adverse(partie["joueur"])
    effacer_terminal()
    afficher_plateau(partie["plateau"])
    return True




def saisir_taille_plateau():
    """ Fait saisir un nombre parmi 4,6 ou 8 (saisie contrôlée).
    :Exemple:
    n = saisir_taille_plateau()
    n est un entier égal à 4, 6 ou 8.
    """
    print("donner la taille du plateau :")
    print("la taille du plateau peut etre 4, 6 ou 8")
    taille = input()
    while taille != '4' and taille != '6' and taille != '8' :
        print("donner la taille du plateau :")
        print("la taille du plateau peut etre 4, 6 ou 8")
        taille = input()
    return int(taille)



def sauvegarder_partie(partie):
    """ Sauvegarde la partie passée en paramètre au format json
    dans le fichier sauvegarde_partie.json
    :Exemple:
    p = creer_partie(4)
    sauvegarder_partie(p)
    Le fichier sauvegarde_partie.json doit contenir :
    {"joueur": 1, "plateau": {"n": 4, "cases": [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0,
    0, 0, 0, 0]}}
    """
    with open("sauvegarde_partie.json", 'w') as f:
        dump(partie, f)



def charger_partie():
    """ Crée la partie à partir des données du fichier sauvegarde_partie.json
    ou crée une nouvelle partie 4*4.
    Retourne la partie créée.
    :Exemple:
    p = charger_partie()
    Si le fichier sauvegarde_partie.json contient :
    {"joueur": 1, "plateau": {"n": 4, "cases": [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0,
    0, 0, 0, 0]}}
    alors p correspond à une nouvelle partie
    """
    if os.path.exists("sauvegarde_partie.json"):
        with open("sauvegarde_partie.json", 'r') as f:
            partie = load(f)
        return partie
    print("aucune partie sauvegardée, un nouvel Othellier de taille 4 sera créé")
    partie = creer_partie(4)
    return partie







def othello():
    """ Fonction permettant de jouer à Othello. On peut enchaîner, sauvegarder,
    charger et recommencer des parties d'Othello.
    :Exemple:
    othello()
    """
    partie = None
    action = saisir_action(partie)
    partie = menu(partie, action)
    effacer_terminal()
    afficher_plateau(partie["plateau"])
    while 1:
        if not jouer(partie):
            action = saisir_action(partie)
            partie = menu(partie, action)
        else :
            dico_resultat = {0: "égalité", 1: "le gagnant est le joueur 1 (noir)", 2: "le gagnant est  le joueur 2 (blanc)"}
            print(dico_resultat[gagnant(partie["plateau"])])
            othello()
