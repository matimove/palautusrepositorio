class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""
        points_dct = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Fourty", 4:"Deuce"}
        minus_result_dct = {1: "Advantage player1", -1: "Advantage player2", 2: "Win for player1"}

        if self.m_score1 == self.m_score2:
            if self.m_score1 < 4:
                score = points_dct[self.m_score1] + "-All"
            else: #If Deuce not adding "-All" to the end
                score = points_dct[self.m_score1]

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2
            if minus_result in minus_result_dct:
                score = minus_result_dct[minus_result]
            else:
                score = "Win for player2"
        else:
            score = points_dct[self.m_score1] + "-" + points_dct[self.m_score2] 

        return score
