from Team import Team
from Player import Player
from Result import Result

class Tournament(object):

    def __init__(self, location : str, tournamentType : int):
        self.location = location
        self.tournamentType = tournamentType
        self.results = []

    def addResult(self, rank : int, team : Team, points : int):
        self.results.append(Result(rank, team, points))

    def getResults(self):
        return self.results
    
    def getLocation(self):
        return self.location
    
    def getTournamentType(self):
        return self.tournamentType
        
    def printTournament(self):
        print(f'Location: {self.location}\n')
        print(f'Tournament Type: {self.tournamentType}\n')
        print("Teams:")
        for team in self.teams:
            team.printTeam()
        print()
        print("Players:")
        for player in self.players:
            player.printPlayer()
        print()


def equals(tournament1 : Tournament, tournament2 : Tournament):
    if tournament1.location != tournament2.getLocation():
        return False
    if tournament1.tournamentType != tournament2.getTournamentType():
        return False
    return True