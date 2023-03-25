


class Player(object):

    def __init__(self, name):
        self.name = name
        self.tournaments = []
        self.teams = []
        self.results = []

    def addTournament(self, tournament):
        if tournament not in self.tournaments:
            self.tournaments.append(tournament)

    def addTeam(self, team):
        if team not in self.teams:
            self.teams.append(team)

    def addResult(self, amount):
        index = 0
        while index < len(self.results) and amount < self.results[index]:
            index += 1
        self.results.insert(index, amount)

    def getName(self):
        return self.name

    def getTournaments(self):
        return self.tournaments
    
    def getTeams(self):
        return self.teams
    
    def getResults(self):
        return self.results

    def equals(self, player):
        if self.name == player.name:
            return True
        else:
            return False
        
    def printPlayer(self):
        print(f'Name: {self.name}')
        print(f'Teams: {self.teams}')
        print(f'Tournaments: {self.tournaments}')
        print(f'Results: {self.results}')
        print()