from Result import Result

class Player(object):

    def __init__(self, name : str):
        self.name = name
        self.results = []

    def addResult(self, rank : int, amount : int, location : str):
        index = 0
        while index < len(self.results) and amount < self.results[index].getPoints():
            index += 1
        self.results.insert(index, Result(rank, amount, location))

    def getName(self):
        return self.name
    
    def getResults(self):
        return self.getResultOne() + self.getResultTwo() + self.getResultThree()
    
    def getResultOne(self):
        if len(self.results) < 1:
            return 0
        return self.results[0].getPoints()
    
    def getResultTwo(self):
        if len(self.results) < 2:
            return 0
        return self.results[1].getPoints()
    
    def getResultThree(self):
        if len(self.results) < 3:
            return 0
        return self.results[2].getPoints()
    
    def getResultByLocation(self, location):
        for result in self.results:
            if result.getLocation() == location:
                return result.getPoints()
        return 0

    def printPlayer(self):
        print(f'Name: {self.name}')
        print(f'Results: {self.results}')
        print()


def equals(player1 : Player, player2 : Player):
    if player1.name != player2.name:
        return False
    return True
    