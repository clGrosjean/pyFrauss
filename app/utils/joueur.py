class Player:
    def __init__(self):
        self.pseudo = ""
        self.score = 0

    def getPseudo(self):
        return self.pseudo

    def getScore(self):
        return self.score

    def setPseudo(self, pseudo):
        self.pseudo = pseudo

    def setScore(self, score):
        self.score = score
