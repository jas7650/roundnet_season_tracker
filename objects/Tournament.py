from objects.Team import Team
from objects.TournamentResult import TournamentResult

class Tournament(object):

    def __init__(self, location : str, tournamentType : int, year : int):
        self.location = location
        self.tournamentType = tournamentType
        self.year = year
        self.results = []

    def addResult(self, rank : int, points : int, team : Team):
        index = 0
        while index < len(self.results) and points < self.results[index].getPoints():
            index += 1
        self.results.insert(index, TournamentResult(rank, points, team))

    def getResults(self):
        return self.results
    
    def getTopThree(self):
        return [self.results[0].getTeam(), self.results[1].getTeam(), self.results[2].getTeam()]
    
    def getLocation(self):
        return self.location
    
    def getTournamentType(self):
        return self.tournamentType
    
    def getYear(self):
        return self.year
        
    def printTournament(self):
        print(f'Location: {self.location}\n')
        print(f'Tournament Type: {self.tournamentType}\n')
        print()
        