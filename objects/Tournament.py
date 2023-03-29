from objects.Team import Team
from objects.TournamentResult import TournamentResult

class Tournament(object):

    def __init__(self, location : str, tournamentType : int, year : int):
        self.location = location
        self.tournamentType = tournamentType
        self.year = year
        self.results = []

    def addResult(self, rank : int, points : int, team : Team):
        self.results.append(TournamentResult(rank, points, team))

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


def equals(tournament1 : Tournament, tournament2 : Tournament):
    if tournament1.getLocation() != tournament2.getLocation():
        return False
    if tournament1.getYear() != tournament2.getYear():
        return False
    return True