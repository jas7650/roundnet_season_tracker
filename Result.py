from Team import Team

class Result(object):

    def __init__(self, rank : int, team : Team, points : int):
        self.rank = rank
        self.team = team
        self.points = points

    def getRank(self):
        return self.rank
    
    def getTeam(self):
        return self.team
    
    def getPoints(self):
        return self.points