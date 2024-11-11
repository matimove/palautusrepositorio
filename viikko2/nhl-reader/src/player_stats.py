class PlayerStats:
    def __init__(self,player_list):
        self.players = player_list

    def top_scorers_by_nationality(self, nationality):
        print(print("Players from " + nationality + ":"))
        players = []
        for player in self.players:
            if player.nationality == nationality:
                players.append(player)

        players.sort(key=lambda player: player.goals + player.assists, reverse=True)
        return players