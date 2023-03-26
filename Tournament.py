from Player import Player
from Team import Team


class Tournament(object):

    def __init__(self, location, tournamentType):
        self.location = location
        self.tournamentType = tournamentType
        self.teams = []
        self.results = []

    def addTournament(self, tournament):
        if tournament not in self.tournaments:
            self.tournaments.append(tournament)

    def addResult(self, amount):
        index = 0
        while index < len(self.points) and amount < self.points[index]:
            index += 1
        self.points.insert(index, amount)

    def addTeam(self, team):
        for team_check in self.teams:
            if team.equals(team_check):
                return
        self.teams.append(team)

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
        
    def printTournament(self):
        print(f'Location: {self.location}')
        print(f'Tournament Type: {self.tournamentType}')
        print("Teams:")
        for team in self.teams:
            team.printTeam()
        print(f'Results: {self.results}')
        print()