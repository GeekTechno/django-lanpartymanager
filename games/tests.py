from django.test import TestCase

from .models import Game


class GameModelTest(TestCase):
    """
    Creates two games and checks if both is saved, games should be retrieved in ASC order
    """
    def test_save_and_retrieving_games(self):
        first_game = Game()
        first_game.name = "First game"
        first_game.save()

        second_game = Game()
        second_game.name = "Second game"
        second_game.save()

        saved_games = Game.objects.all()

        self.assertEqual(saved_games.count(), 2)
        self.assertEqual(saved_games[0].name, 'First game')
        self.assertEqual(saved_games[1].name, 'Second game')