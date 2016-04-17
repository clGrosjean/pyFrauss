# -*- coding: utf-8 -*-

import socket
import threading


class ThreadReception(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        while True:
            try:
                response = self.connexion.recv(1024)
                response = response.decode(encoding='UTF-8')
            except socket.error:
                pass


class ThreadEmission(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        while True:
            try:
                message = input()
            except:
                pass
