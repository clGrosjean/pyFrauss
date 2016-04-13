# -*- coding: UTF-8 -*-

import math
import random

# i = 5
# secret = 42
# nombre = 40
# mentir = True
# message = 42
def reponse(message, mentir):
    if message == 42:
        print("Bravo tu as réussi")
    elif message == 1 and mentir == True:## 1 == trop grand
        print("nombre petit, recommence cela ne fait que la {0} fois que tu recommence".format(i))
    elif message == 1 and mentir == False:## 1 == trop grand
        print("nombre  grand, recommence cela ne fait que la {0} fois que tu recommence".format(i))
    elif message == 2 and mentir == True:## 2 == trop petit
        print("nombre  grand, recommence cela ne fait que la {0} fois que tu recommence".format(i))
    else:##2 ==trop petit
        print("nombre petit, recommence cela ne fait que la {0} fois que tu recommence".format(i))


def message(secret, nombre):
    if secret == nombre:
        return 42
    elif secret < nombre:
        return 1
    else: return 2

def aleat(level):
    return random.randint(0,level)

def liste_mensonge(taux_mensonge):
    B, k = [], 0
    A = [False for i in range(100)]
    while k <= taux_mensonge:
        aleat_mensonge = random.randint(0,99)
        if B.count(aleat_mensonge) == 0:
            B += [aleat_mensonge]
            A[aléat_mensonge] = True
            k += 1
        else:
            pass
