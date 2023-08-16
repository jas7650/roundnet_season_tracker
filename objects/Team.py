from objects.Player import Player
from objects.Result import Result


class Team(object):

    def __init__(self, teamName : str, player_one: Player, player_two: Player):
        self.teamName = teamName
        self.players = [player_one, player_two]
        self.proBid = False
        self.results = {}

    def addResult(self, rank : int, amount : int, location : str, year : int):
        index = 0
        if year in self.results.keys():
            year_results = self.results[year]
            while index < len(year_results) and amount < year_results[index].getPoints():
                index += 1
            self.results[year].insert(index, Result(rank, amount, location))
        else:
            self.results[year] = [Result(rank, amount, location)]

    def setProBid(self):
        self.proBid = True

    def getProBid(self):
        return self.proBid

    def getTeamName(self):
        return self.teamName

    def getPoints(self):
        return self.getResultOne() + self.getResultTwo() + self.getResultThree()

    def getResultOne(self):
        results = []
        for year in self.results.keys():
            for result in self.results[year]:
                results.append(result)
        results = sorted(results, key=lambda x: x.getPoints(), reverse=True)
        if len(results) < 1:
            return 0
        return results[0].getPoints()

    def getResultTwo(self):
        results = []
        for year in self.results.keys():
            for result in self.results[year]:
                results.append(result)
        results = sorted(results, key=lambda x: x.getPoints(), reverse=True)
        if len(results) < 2:
            return 0
        return results[1].getPoints()

    def getResultThree(self):
        results = []
        for year in self.results.keys():
            for result in self.results[year]:
                results.append(result)
        results = sorted(results, key=lambda x: x.getPoints(), reverse=True)
        if len(results) < 3:
            return 0
        return results[2].getPoints()

    def getResultByLocation(self, location, year):
        if year in self.results.keys():
            for result in self.results[year]:
                if result.getLocation() == location:
                    return result.getPoints()
        return 0

    def getPointsYear(self, year : str):
        return self.getResultOneYear(year) + self.getResultTwoYear(year) + self.getResultThreeYear(year)

    def getResultOneYear(self, year : int):
        results = []
        if year in self.results.keys():
            for result in self.results[year]:
                results.append(result)
        results = sorted(results, key=lambda x: x.getPoints(), reverse=True)
        if len(results) < 1:
            return 0
        return results[0].getPoints()

    def getResultTwoYear(self, year : int):
        results = []
        if year in self.results.keys():
            for result in self.results[year]:
                results.append(result)
        results = sorted(results, key=lambda x: x.getPoints(), reverse=True)
        if len(results) < 2:
            return 0
        return results[1].getPoints()

    def getResultThreeYear(self, year : int):
        results = []
        if year in self.results.keys():
            for result in self.results[year]:
                results.append(result)
        results = sorted(results, key=lambda x: x.getPoints(), reverse=True)
        if len(results) < 3:
            return 0
        return results[2].getPoints()

    def getPlayerNames(self):
        return [self.getPlayerOne().getName(), self.getPlayerTwo().getName()]

    def getPlayers(self):
        return self.players

    def getPlayerOne(self):
        return self.players[0]

    def getPlayerTwo(self):
        return self.players[1]

    def printTeam(self):
        print(f'Team Name: {self.teamName}')
        print(f'Players: {self.getPlayerOne().getName()} and {self.getPlayerTwo().getName()}')
        points = []
        for result in self.results:
            points.append(result.getPoints())
        print(f'Points: {points}')
        print(f'Pro Bid: {self.proBid}')
        print()
