class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.nationality = dict["nationality"]
        self.goals = dict['goals']
        self.assists = dict['assists']
    
    def __str__(self):
        result = f"{self.name:20}" + f"{self.team:5}" +  str(self.goals) + " + " + str(self.assists) + " = " + str(self.goals + self.assists)
        return result