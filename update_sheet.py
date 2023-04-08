from utils.scrape_utils import *
from utils.sheet_utils import *
from utils.path_utils import *
from utils.point_utils import *
from utils.compare_utils import *
from objects.Player import Player
from objects.Tournament import Tournament
from objects.Team import Team

RANK = 1
TEAM = 2
PLAYER_ONE = 3
PLAYER_TWO = 4
POINTS = 5

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
    readYearDirectory(tourney_path, 2023)

    filename = 'roundnet_season_tracker.xlsx'

    createPlayersSheet(filename)
    createPlayersRankedSheet(filename)
    createTeamsSheet(filename)
    createTeamsRankedSheet(filename)
    createProBidsSheet(filename)
    createTournamentSheets(filename)


def readYearDirectory(tourney_path, year):
    print(f'Year: {year}')
    year_path = joinPath(tourney_path, str(year))
    if (pathExists(year_path)):
        readDirectory(os.path.join(year_path, "sts", "championship"), year)
        readDirectory(os.path.join(year_path, "sts", "major"), year)
        readDirectory(os.path.join(year_path, "sts", "challenger"), year)
        readDirectory(os.path.join(year_path, "sts", "contender"), year)
    print()


def readDirectory(path, year):
    if (pathExists(path)):
        for filename in listDir(path):
            folder = joinPath(path, filename)
            if not isFile(folder):
                processTournament(folder, year)


def processTournament(path, year):
    location = os.path.basename(path)
    tournament_type = getTournamentType(os.path.basename(os.path.dirname(path)))

    location = splitText(getBaseName(path))[0]
    location = location.replace("_", " ")

    tournament = Tournament(location, tournament_type, year)
    print(f'{location}: {year}')

    if not tournamentExists(tournament):
        tournaments_list.append(tournament)

    tournaments_index = getTournamentIndex(tournament)

    divisions = []
    for filename in os.listdir(path):
        divisions.append(str(filename).split(".")[0])

    for division in divisions:
        if division == "contender" and "premier" in divisions:
            continue
        ranks, teams = scrapeFile(os.path.join(path, f"{division}.html"))
        if division == "premier" and tournament_type == TournamentType.CHAMPIONSHIP.value:
            for i in range(len(ranks)):
                ranks[i] += 16
        points = getPoints(tournament_type, year, ranks, len(teams[0]))

        for i in range(len(teams[0])):
            player_one = Player(teams[1][i])
            player_two = Player(teams[2][i])

            if not playerExists(player_one):
                players_list.append(player_one)    

            if not playerExists(player_two):
                players_list.append(player_two)

            p1_index = getPlayerIndex(player_one)
            p2_index = getPlayerIndex(player_two)
            if i >= len(points):
                players_list[p1_index].addResult(ranks[i], 0, location)
                players_list[p2_index].addResult(ranks[i], 0, location)
            else:
                players_list[p1_index].addResult(ranks[i], points[i]/2.0, location)
                players_list[p2_index].addResult(ranks[i], points[i]/2.0, location)
            

            team = Team(teams[0][i], player_one, player_two)

            if not teamExists(team):
                teams_list.append(team)
                
            team_index = getTeamIndex(team)

            teams_list[team_index].addResult(ranks[i], points[i], location)
            tournaments_list[tournaments_index].addResult(ranks[i], points[i], teams_list[team_index])
        if tournament.getTournamentType() == TournamentType.MAJOR.value:
            if year == 2023:
                top_three = tournament.getTopThree()
                for team in top_three:
                    for i in range(len(teams_list)):
                        if team_equals(team, teams_list[i]):
                            teams_list[i].setProBid()    


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

        wb = writeToSheet(data, wb, f'{tournament.getLocation()} {tournament.getYear()}')
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
    copy_list = []
    for player in players_list:
        copy_list.append(player)
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
    sorted_list = []

    copy_list = teams_list.copy()
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


def createProBidsSheet(filename : str):
    wb = getWorkBook(filename)
    team_names = ['Team']
    player_ones = ['Player One']
    player_twos = ['Player Two']
    points = ['Points']
    pro_bids = ['Pro Bid']
    pro_bids_list = []
    sorted_list = []

    copy_list = teams_list.copy()
    for team in teams_list:
        if team.getProBid() == True:
            pro_bids_list.append(team)
            copy_list.remove(team)
    remaining_spots = 16-len(pro_bids_list)
    for i in range(remaining_spots):
        largest_team = copy_list[0]
        for team in copy_list:
            if team.getPoints() > largest_team.getPoints():
                largest_team = team
        copy_list.remove(largest_team)
        pro_bids_list.append(largest_team)

    copy_list = pro_bids_list.copy()
    for i in range(16):
        largest_team = copy_list[0]
        for team in copy_list:
            if team.getPoints() > largest_team.getPoints():
                largest_team = team
        copy_list.remove(largest_team)
        sorted_list.append(largest_team)

    for team in sorted_list:
        team_names.append(team.getTeamName())
        player_ones.append(team.getPlayerOne().getName())
        player_twos.append(team.getPlayerTwo().getName())
        points.append(team.getPoints())
        pro_bids.append(team.getProBid())
    data = [team_names, player_ones, player_twos, points, pro_bids]

    wb = writeToSheet(data, wb, 'Pro Bids')
    saveWorkBook(wb, filename)    


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
        if team_equals(team_check, team):
            return True
    return False


def getTeamIndex(team : Team):
    for i in range(len(teams_list)):
        team_check = teams_list[i]
        if team_equals(team_check, team):
            return i
        

def playerExists(player : Player):
    for player_check in players_list:
        if player_equals(player_check, player):
            return True
    return False


def getPlayerIndex(player : Player):
    for i in range(len(players_list)):
        player_check = players_list[i]
        if player_equals(player_check, player):
            return i
        

def tournamentExists(tournament : Tournament):
    for tournament_check in tournaments_list:
        if tournaments_equals(tournament_check, tournament):
            return True
    return False


def getTournamentIndex(tournament : Tournament):
    for i in range(len(tournaments_list)):
        tournament_check = tournaments_list[i]
        if tournaments_equals(tournament_check, tournament):
            return i


if __name__ == "__main__":
    main()
