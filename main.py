# -*- coding: UTF-8 -*-

import random
import time

def reponse(message, mentir, i, temps_de_partie):
    if message == 42:
        print("Bravo tu as réussi en {0} essai et tu as mis {1} secondes".format(i, int(
            time.perf_counter() - temps_de_partie)))
        return 42
    elif message == 1 and mentir == True:  ## 1 == trop grand
        print("nombre petit, recommence cela ne fait que la {0} fois que tu recommence".format(i))
    elif message == 1 and mentir == False:  ## 1 == trop grand
        print("nombre  grand, recommence cela ne fait que la {0} fois que tu recommence".format(i))
    elif message == 2 and mentir == True:  ## 2 == trop petit
        print("nombre  grand, recommence cela ne fait que la {0} fois que tu recommence".format(i))
    else:  ##2 == trop petit
        print("nombre petit, recommence cela ne fait que la {0} fois que tu recommence".format(i))


def message(secret, nombre):
    if secret == nombre:
        return 42
    elif secret < nombre:
        return 1
    else:
        return 2


def aleat(level):
    return random.randint(0, level)


def liste_mensonge(taux_mensonge, niveau_indication):
    B, k = [], 0
    annoce_mensonge(taux_mensonge, niveau_indication)
    A = [False for i in range(100)]
    while k <= taux_mensonge:
        aleat_mensonge = random.randint(0, 99)
        if B.count(aleat_mensonge) == 0:
            B += [aleat_mensonge]
            A[aleat_mensonge] = True
            k += 1
        else:
            pass
    return A


def exponentiation_rapide(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return exponentiation_rapide(x * x, n / 2)
    return x * exponentiation_rapide(x * x, (n - 1) / 2)


def mentir(A, t):
    a = random.randint(0, 99)
    t1 = (time.perf_counter() - t) * exponentiation_rapide(10, 16) + a
    p = int(t1 % len(A))
    return A[p]


def annoce_mensonge(taux_mensonge, niveau_indication):
    if niveau_indication <= 0:
        pass
    elif niveau_indication == 1:
        if taux_mensonge >= 80:
            print("The cake is a lie")
        elif taux_mensonge < 80 and taux_mensonge >= 50:
            print("Ne crois pas tout ce que l'on peut te dire")
        elif taux_mensonge < 50 and taux_mensonge >= 20:
            print("L'erreur est humain :D")
        else:
            print("L'IA est la pour t'aider tu sais ?")
    else:
        print("tu as {0} % de chance d'avoir une fausse information".format(taux_mensonge))


def jeux():
    print(
        " <Le mode de jeux: solo>\n\nMerci de choisir le niveau d'indication sur le taux de mensonge:\nTaper 0 pour aucune indication\nTaper 1 pour avoir une petite indication\nTaper 2 pour avoir le taux précis\n")
    niveau_indication = int(input())
    SECRET = aleat(100)
    A, i, r = liste_mensonge(random.randint(0, 100), niveau_indication), 1, 0
    print("Début du jeu\n")
    temps_de_partie = time.perf_counter()
    while True:
        t = time.perf_counter()
        nbr_joueur = int(input())
        r = reponse(message(SECRET, nbr_joueur), mentir(A, t), i, temps_de_partie)
        if r == 42:
            break
        i += 1


jeux()
