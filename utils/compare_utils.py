from objects.Tournament import Tournament
from objects.Team import Team
from objects.Player import Player


def player_equals(player1 : Player, player2 : Player):
    if player1.name != player2.name:
        return False
    return True

def team_equals(team1 : Team, team2 : Team):
    if team1.teamName != team2.teamName:
        return False
    if team1.getPlayerOne().getName() not in team2.getPlayerNames():
        return False
    if team1.getPlayerTwo().getName() not in team2.getPlayerNames():
        return False
    return True

def tournaments_equals(tournament1 : Tournament, tournament2 : Tournament):
    if tournament1.getLocation() != tournament2.getLocation():
        return False
    if tournament1.getYear() != tournament2.getYear():
        return False
    return True
