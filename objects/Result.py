
class Result(object):

    def __init__(self, rank : int, points : int, location : str):
        self.rank = rank
        self.points = points
        self.location = location

    def getRank(self):
        return self.rank
    
    def getPoints(self):
        return self.points
    
    def getLocation(self):
        return self.location