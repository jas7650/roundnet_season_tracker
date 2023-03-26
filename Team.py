from Player import Player


class Team(object):

    def __init__(self, teamName, player_one, player_two):
        self.teamName = teamName
        self.players = [player_one, player_two]
        self.tournaments = []
        self.teams = []
        self.points = []

    def addTournament(self, tournament):
        if tournament not in self.tournaments:
            self.tournaments.append(tournament)

    def addResult(self, amount):
        index = 0
        while index < len(self.points) and amount < self.points[index]:
            index += 1
        self.points.insert(index, amount)

    def getTeamName(self):
        return self.teamName

    def getTournaments(self):
        return self.tournaments
    
    def getResults(self):
        return self.points
    
    def getPlayers(self):
        return self.players

    def equals(self, team):
        if self.teamName != team.teamName:
            return False
        if team.getPlayers()[0] not in self.players:
            return False
        if team.getPlayers()[1] not in self.players:
            return False
        return True
        
    def printTeam(self):
        print(f'Name: {self.teamName}')
        print(f'Players: {self.players[0]} and {self.players[1]}')
        print(f'Tournaments: {self.tournaments}')
        print(f'Points: {self.points}')
        print()