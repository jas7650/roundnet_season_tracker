from Team import Team
class TournamentResult(object):

    def __init__(self, rank : int, points : int, team : Team):
        self.rank = rank
        self.points = points
        self.team = team

    def getRank(self):
        return self.rank
    
    def getPoints(self):
        return self.points
    
    def getTeam(self):
        return self.team