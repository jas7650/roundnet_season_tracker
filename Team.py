from Player import Player


class Team(object):

    def __init__(self, teamName : str, player_one: Player, player_two: Player):
        self.teamName = teamName
        self.players = [player_one, player_two]
        self.points = []

    def addResult(self, amount : int):
        index = 0
        while index < len(self.points) and amount < self.points[index]:
            index += 1
        self.points.insert(index, amount)

    def getTeamName(self):
        return self.teamName
    
    def getResults(self):
        return self.points
    
    def getPlayers(self):
        return self.players
    
    def getPlayerOne(self):
        return self.players[0]
    
    def getPlayerTwo(self):
        return self.players[1]
        
    def printTeam(self):
        print(f'Team Name: {self.teamName}')
        print(f'Players: {self.getPlayerOne().getName()} and {self.getPlayerTwo().getName()}')
        print(f'Points: {self.points}')
        print()

def equals(team1 : Team, team2 : Team):
    if team1.teamName != team2.teamName:
        return False
    if team1.getPlayers()[0] not in team2.players:
        return False
    if team1.getPlayers()[1] not in team2.players:
        return False
    return True