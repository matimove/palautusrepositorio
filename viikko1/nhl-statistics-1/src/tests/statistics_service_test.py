import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_pelaaja_haku_toimii(self):
        self.assertEqual(str(self.stats.search("Kurri")), "Kurri EDM 37 + 53 = 90")

    
    def test_tiimi_haku_toimii(self):
    
        self.assertEqual([player.name for player in self.stats.team("EDM")], ['Semenko', 'Kurri', 'Gretzky'])

    def test_näytetään_ensimmäiset_n_pelaajaa(self):
    
        self.assertEqual([player.name for player in self.stats.top(2)], ['Gretzky', 'Lemieux', 'Yzerman'])

    def test_haetaan_olematonta_pelaajaa(self):
        self.assertEqual(str(self.stats.search("Karri")), "None")