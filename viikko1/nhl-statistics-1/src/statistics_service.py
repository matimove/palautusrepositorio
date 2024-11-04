from player_reader import PlayerReader

from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, readeri):
        reader = readeri

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, ordering_criteria):

        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by(player, ordering_criteria):
            if ordering_criteria == SortBy.POINTS:
                return player.points
            elif ordering_criteria == SortBy.GOALS:
                return player.goals
            elif ordering_criteria == SortBy.ASSISTS:
                return player.assists
            
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
