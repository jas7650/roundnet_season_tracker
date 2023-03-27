

class Player(object):

    def __init__(self, name : str):
        self.name = name
        self.points = []

    def addResult(self, amount : int):
        index = 0
        while index < len(self.points) and amount < self.points[index]:
            index += 1
        self.points.insert(index, amount)

    def getName(self):
        return self.name
    
    def getResults(self):
        return self.points

    def printPlayer(self):
        print(f'Name: {self.name}')
        print(f'Points: {self.points}')
        print()


def equals(player1 : Player, player2 : Player):
    if player1.name != player2.name:
        return False
    return True
    