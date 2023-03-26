from scrape_utils import *
from sheet_utils import *
from path_utils import *
from Player import Player
from Tournament import Tournament
from Team import Team

RANK = 1
TEAM = 2
PLAYER_ONE = 3
PLAYER_TWO = 4
POINTS = 5

CONTENDER = 0
CHALLENGER = 1 
MAJOR = 2
CHAMPIONSHIP_PRO = 3
CHAMPIONSHIP_PREMIER = 4

PLAYER_COL = 1
POINTS_COL = 2


def main():
   
    tourney_path = joinPath(getCurrentLocation(), "tournaments")
    path_2022 = joinPath(tourney_path, "2022")
    challenger_path = joinPath(path_2022, "challenger")
    atlanta_path = joinPath(challenger_path, "Atlanta.html")
    processTournament(atlanta_path, CHALLENGER)

    
    
    # wb = readYearDirectory(wb, tourney_path, 2022)  
    # wb = readYearDirectory(wb, tourney_path, 2023)

def processTournament(path, TOURNAMENT_TYPE):
    location = splitText(getBaseName(path))[0]
    location = location.replace("_", " ")

    tournament = Tournament(location, TOURNAMENT_TYPE)
    ranks, teams = scrapeFile(path)
    ideal_points = getPointsArray(2022, TOURNAMENT_TYPE)
    old_points = getActualPoints(ranks, ideal_points)
    points = []
    for value in old_points:
        points.append(value/2.0)

    for i in range(len(teams[0])):
        team = Team(teams[0][i], teams[1][i], teams[2][i])
        team.addResult(points[i])
        tournament.addTeam(team)
    tournament.printTournament()
    
    # players = addPlayers(teams, points, location)
    # print("Players")
    # for player in players:
    #     player.printPlayer()


def readYearDirectory(wb, tourney_path, year):
    print(f'Year: {year}')
    year_path = joinPath(tourney_path, str(year))
    if (pathExists(year_path)):
        wb = readDirectory(wb, joinPath(year_path, joinPath("championship", "pro")), CHAMPIONSHIP_PRO)
        wb = readDirectory(wb, joinPath(year_path, "major"), MAJOR)
        wb = readDirectory(wb, joinPath(year_path, joinPath("championship", "premier")), CHAMPIONSHIP_PREMIER)
        wb = readDirectory(wb, joinPath(year_path, "challenger"), CHALLENGER)
        wb = readDirectory(wb, joinPath(year_path, "contender"), CONTENDER)
    return wb


def readDirectory(wb, path, TOURNAMENT_TYPE):
    if (pathExists(path)):
        for filename in listDir(path):
            file = joinPath(path, filename)
            if isFile(file):
                ranks, teams = scrapeFile(file)
                if (TOURNAMENT_TYPE == CHAMPIONSHIP_PREMIER):
                    for i in range(len(ranks)):
                        ranks[i] = ranks[i]+16
                location = splitText(getBaseName(file))[0]
                location = location.replace("_", " ")
                print(location)
                ideal_points = getPointsArray(2022, TOURNAMENT_TYPE)
                old_points = getActualPoints(ranks, ideal_points)
                points = []
                for value in old_points:
                    points.append(value/2.0)
                players = addPlayers(teams, points, location)
                print("Players")
                for player in players:
                    player.printPlayer()
    return wb


def addPlayers(teams, points, location):
    players = []
    for i in range(len(points)):
        player_one = Player(teams[1][i])
        player_one.addTeam(teams[0][i])
        player_one.addTournament(location)
        player_one.addResult(points[i])
        player_two = Player(teams[2][i])
        player_two.addTeam(teams[0][i])
        player_two.addTournament(location)
        player_two.addResult(points[i])
        players.append(player_one)
        players.append(player_two)

    return players


def getPointsArray(year, TOURNAMENT_TYPE):
    wb = getWorkBook('point_distribution.xlsx')
    
    if (year == 2022):
        sheet = getSheetByName(wb, 'Point Distribution 2022')
    else:
        sheet = getSheetByName(wb, 'Point Distribution 2023')
    if (TOURNAMENT_TYPE == CHAMPIONSHIP_PREMIER):
        column = CHAMPIONSHIP_PRO + 2 
    else:
        column = TOURNAMENT_TYPE + 2
    points = getColumnData(sheet, column)
    return points


def getActualPoints(ranks, points):
    previousRank = 0
    average = 0
    i = 0
    actual_points = []
    if (len(ranks) != len(points)):
        points = points[ranks[0]-1:]
    while (i < len(ranks)):
        rank = ranks[i]
        if (rank != previousRank):
            average = getAverageValue(ranks, points, i)

        actual_points.append(average)
        previousRank = rank
        i = i + 1
    return actual_points


def getAverageValue(ranks, points, index):
    if (index == len(ranks)-1):
        return ranks[index]
    i = index+1
    numValues = 1
    sum = points[index]

    while (ranks[i] == ranks[index]):
        sum += points[i]
        numValues += 1
        i += 1
        if (i == len(ranks)):
            break
    return sum/numValues


if __name__ == "__main__":
    main()
