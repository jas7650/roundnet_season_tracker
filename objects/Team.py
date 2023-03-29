from objects.Player import Player
from objects.Result import Result


class Team(object):

    def __init__(self, teamName : str, player_one: Player, player_two: Player):
        self.teamName = teamName
        self.players = [player_one, player_two]
        self.proBid = False
        self.results = []

    def addResult(self, rank : int, amount : int, location : str):
        index = 0
        while index < len(self.results) and amount < self.results[index].getPoints():
            index += 1
        self.results.insert(index, Result(rank, amount, location))

    def setProBid(self):
        self.proBid = True

    def getProBid(self):
        return self.proBid

    def getTeamName(self):
        return self.teamName
    
    def getPoints(self):
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
    
    def getPlayerNames(self):
        return [self.getPlayerOne().getName(), self.getPlayerTwo().getName()]
    
    def getPlayers(self):
        return self.players
    
    def getPlayerOne(self):
        return self.players[0]
    
    def getPlayerTwo(self):
        return self.players[1]
        
    def printTeam(self):
        print(f'Team Name: {self.teamName}')
        print(f'Players: {self.getPlayerOne().getName()} and {self.getPlayerTwo().getName()}')
        points = []
        for result in self.results:
            points.append(result.getPoints())
        print(f'Points: {points}')
        print(f'Pro Bid: {self.proBid}')
        print()

def equals(team1 : Team, team2 : Team):
    if team1.teamName != team2.teamName:
        return False
    if team1.getPlayerOne().getName() not in team2.getPlayerNames():
        return False
    if team1.getPlayerTwo().getName() not in team2.getPlayerNames():
        return False
    return True