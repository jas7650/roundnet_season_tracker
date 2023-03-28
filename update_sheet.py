from scrape_utils import *
from sheet_utils import *
from path_utils import *
import Player as Player_Class
import Tournament as Tournament_Class
import Team as Team_Class
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
    global players_list
    global teams_list
    global tournaments_list

    players_list = []
    teams_list = []
    tournaments_list = []
   
    tourney_path = joinPath(getCurrentLocation(), "tournaments")

    readYearDirectory(tourney_path, 2022)

    filename = 'roundnet_season_tracker.xlsx'

    createPlayersSheet(filename)
    createPlayersRankedSheet(filename)
    createTeamsSheet(filename)
    createTeamsRankedSheet(filename)
    createTournamentSheets(filename)


def readYearDirectory(tourney_path, year):
    print(f'Year: {year}')
    year_path = joinPath(tourney_path, str(year))
    if (pathExists(year_path)):
        readDirectory(joinPath(year_path, joinPath("championship", "pro")), CHAMPIONSHIP_PRO, year)
        readDirectory(joinPath(year_path, "major"), MAJOR, year)
        readDirectory(joinPath(year_path, joinPath("championship", "premier")), CHAMPIONSHIP_PREMIER, year)
        readDirectory(joinPath(year_path, "challenger"), CHALLENGER, year)
        readDirectory(joinPath(year_path, "contender"), CONTENDER, year)


def readDirectory(path, TOURNAMENT_TYPE, year):
    if (pathExists(path)):
        for filename in listDir(path):
            file = joinPath(path, filename)
            if isFile(file):
                processTournament(file, TOURNAMENT_TYPE, year)


def processTournament(path, TOURNAMENT_TYPE, year):
    location = splitText(getBaseName(path))[0]
    location = location.replace("_", " ")

    tournament = Tournament(location, TOURNAMENT_TYPE)

    print(location)

    if not tournamentExists(tournament):
        tournaments_list.append(tournament)

    tournaments_index = getTournamentIndex(tournament)

    ranks, teams = scrapeFile(path)
    
    if TOURNAMENT_TYPE == CHAMPIONSHIP_PREMIER:
        for i in range(len(ranks)):
            ranks[i] += 16

    ideal_points = getPointsArray(year, TOURNAMENT_TYPE)
    old_points = getActualPoints(ranks, ideal_points)

    points = []
    for value in old_points:
        points.append(value/2.0)

    for i in range(len(teams[0])):
        player_one = Player(teams[1][i])
        player_two = Player(teams[2][i])

        if not playerExists(player_one):
            players_list.append(player_one)    

        if not playerExists(player_two):
            players_list.append(player_two)

        p1_index = getPlayerIndex(player_one)
        p2_index = getPlayerIndex(player_two)
        players_list[p1_index].addResult(ranks[i], points[i], location)
        players_list[p2_index].addResult(ranks[i], points[i], location)

        team = Team(teams[0][i], player_one, player_two)

        if not teamExists(team):
            teams_list.append(team)
            
        team_index = getTeamIndex(team)

        teams_list[team_index].addResult(ranks[i], points[i]*2, location)
        tournaments_list[tournaments_index].addResult(ranks[i], points[i]*2, teams_list[team_index])


def createTournamentSheets(filename : str):
    wb = getWorkBook(filename)
    for tournament in tournaments_list:
        results = tournament.getResults()
        ranks = ['Rank']
        teams = []
        points = ['Points Awarded']
        for result in results:
            ranks.append(result.getRank())
            teams.append(result.getTeam())
            points.append(result.getPoints())
        teamNames = ['Team']
        player_ones = ['Player One']
        player_twos = ['Player Two']
        for team in teams:
            teamNames.append(team.getTeamName())
            player_ones.append(team.getPlayerOne().getName())
            player_twos.append(team.getPlayerTwo().getName())
        data = [ranks, teamNames, player_ones, player_twos, points]

        wb = writeToSheet(data, wb, tournament.getLocation())
        for i in range(len(tournaments_list)):
            tournament = tournaments_list[i]
            tournament_data = [tournament.getLocation()]
            for team in teams_list:
                tournament_data.append(team.getResultByLocation(tournament.getLocation()))
            wb = writeToColumn(tournament_data, wb, 'Teams', i+7)
    saveWorkBook(wb, filename)


def createPlayersSheet(filename : str):
    wb = getWorkBook(filename)
    wb = removeSheets(wb)
    player_names = ['Player']
    points = ['Points']
    result_ones = ['Result 1']
    result_twos = ['Result 2']
    result_threes = ['Result 3']
    for player in players_list:
        player_names.append(player.getName())
        points.append(player.getPoints())
        result_ones.append(player.getResultOne())
        result_twos.append(player.getResultTwo())
        result_threes.append(player.getResultThree())            

    data = [player_names, points, result_ones, result_twos, result_threes]
    wb = writeToSheet(data, wb, 'Players')

    for i in range(len(tournaments_list)):
        tournament = tournaments_list[i]
        tournament_data = [tournament.getLocation()]
        for player in players_list:
            tournament_data.append(player.getResultByLocation(tournament.getLocation()))
        wb = writeToColumn(tournament_data, wb, 'Players', i+5)
    saveWorkBook(wb, filename)


def createPlayersRankedSheet(filename):
    wb = getWorkBook(filename)
    player_names = ['Player']
    points = ['Points']
    copy_list = players_list
    sorted_list = []
    for i in range(len(players_list)):
        largest_player = copy_list[0]
        for player in copy_list:
            if player.getPoints() > largest_player.getPoints():
                largest_player = player
        sorted_list.append(largest_player)
        copy_list.remove(largest_player)

    for player in sorted_list:
        player_names.append(player.getName())
        points.append(player.getPoints())          

    data = [player_names, points]
    wb = writeToSheet(data, wb, 'Players Ranked')
    saveWorkBook(wb, filename)


def createTeamsSheet(filename: str):
    wb = getWorkBook(filename)
    team_names = ['Team']
    player_ones = ['Player One']
    player_twos = ['Player Two']
    points = ['Points']
    result_ones = ['Result 1']
    result_twos = ['Result 2']
    result_threes = ['Result 3']
    for team in teams_list:
        team_names.append(team.getTeamName())
        player_ones.append(team.getPlayerOne().getName())
        player_twos.append(team.getPlayerTwo().getName())
        points.append(team.getPoints())
        result_ones.append(team.getResultOne())
        result_twos.append(team.getResultTwo())
        result_threes.append(team.getResultThree())
    data = [team_names, player_ones, player_twos, points, result_ones, result_twos, result_threes]
    wb = writeToSheet(data, wb, 'Teams')
    for i in range(len(tournaments_list)):
        tournament = tournaments_list[i]
        tournament_data = [tournament.getLocation()]
        for team in teams_list:
            tournament_data.append(team.getResultByLocation(tournament.getLocation()))
        wb = writeToColumn(tournament_data, wb, 'Teams', i+7)
    saveWorkBook(wb, filename)


def createTeamsRankedSheet(filename):
    wb = getWorkBook(filename)
    team_names = ['Team']
    player_ones = ['Player One']
    player_twos = ['Player Two']
    points = ['Points']
    copy_list = teams_list
    sorted_list = []
    for i in range(len(teams_list)):
        largest_team = copy_list[0]
        for team in copy_list:
            if team.getPoints() > largest_team.getPoints():
                largest_team = team
        sorted_list.append(largest_team)
        copy_list.remove(largest_team)

    for team in sorted_list:
        team_names.append(team.getTeamName())
        player_ones.append(team.getPlayerOne().getName())
        player_twos.append(team.getPlayerTwo().getName())
        points.append(team.getPoints())          

    data = [team_names, player_ones, player_twos, points]
    wb = writeToSheet(data, wb, 'Teams Ranked')
    saveWorkBook(wb, filename)


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


def printTeams():
    print("Teams:")
    for team in teams_list:
        team.printTeam()


def printPlayers():
    print("Players:")
    for player in players_list:
        player.printPlayer()


def teamExists(team : Team):
    for team_check in teams_list:
        if Team_Class.equals(team_check, team):
            return True
    return False


def getTeamIndex(team : Team):
    for i in range(len(teams_list)):
        team_check = teams_list[i]
        if Team_Class.equals(team_check, team):
            return i
        

def playerExists(player : Player):
    for player_check in players_list:
        if Player_Class.equals(player_check, player):
            return True
    return False


def getPlayerIndex(player : Player):
    for i in range(len(players_list)):
        player_check = players_list[i]
        if Player_Class.equals(player_check, player):
            return i
        

def tournamentExists(tournament : Tournament):
    for tournament_check in tournaments_list:
        if Tournament_Class.equals(tournament_check, tournament):
            return True
    return False


def getTournamentIndex(tournament : Tournament):
    for i in range(len(tournaments_list)):
        tournament_check = tournaments_list[i]
        if Tournament_Class.equals(tournament_check, tournament):
            return i


if __name__ == "__main__":
    main()
