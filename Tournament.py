from Team import Team
from TournamentResult import TournamentResult

class Tournament(object):

    def __init__(self, location : str, tournamentType : int):
        self.location = location
        self.tournamentType = tournamentType
        self.results = []

    def addResult(self, rank : int, points : int, team : Team):
        self.results.append(TournamentResult(rank, points, team))

    def getResults(self):
        return self.results
    
    def getLocation(self):
        return self.location
    
    def getTournamentType(self):
        return self.tournamentType
        
    def printTournament(self):
        print(f'Location: {self.location}\n')
        print(f'Tournament Type: {self.tournamentType}\n')
        print()


def equals(tournament1 : Tournament, tournament2 : Tournament):
    if tournament1.getLocation() != tournament2.getLocation():
        return False
    return True