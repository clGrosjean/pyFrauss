# -*- coding: utf-8 -*-

import socket
import sys
import threading

HOST = ""
PORT = 12345

MIN_JOUEUR = 2


class ThreadClients(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

        self.name = self.getName()
        clients[self.name] = self.connexion

        print("Connexion du client {0} {1} {2}".format(self.connexion.getpeername(), self.name, self.connexion))
        self.connexion.send(b"Vous etes bien connecte au serveur.\n", "utf-8")

    def run(self):
        self.connexion.send(b"Entrez votre pseudo :\n")
        pseudo = self.connexion.recv(1024)
        pseudo = pseudo.decode(encoding='UTF-8')

        print("Pseudo du client {0} > {1}".format(self.connexion.getpeername(), pseudo))
        self.connexion.send(b"En attente d'autres joueurs...\n")

        ''' Attente réponse client '''
        while True:
            response = self.connexion.recv(1024)
            response = response.decode(encoding='UTF-8')

        self.connexion.close()
        del clients[self.name]
        print("Client {0} déconnecté.".format(self.name))


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    mySocket.bind((HOST, PORT))
except:
    print("La liaison du socket à l'adresse choisie à échoué")
    sys.exit()
else:
    print("Serveur prêt (port {0}) en attente de clients ...".format(PORT))
    mySocket.listen(5)

clients = {}
while len(clients) < MIN_JOUEUR:
    connexion, adresse = mySocket.accept()
    th = ThreadClients(connexion)
    th.setDaemon(1)
    th.start()

for client in clients:
    clients[client].send(b"\nLa partie va commencer !\n", "UTF-8")

