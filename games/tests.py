from datetime import datetime, timedelta
from time import sleep

from django.test import TestCase

from .models import Instruction, Game


def create_game(name):
    return Game.objects.create(name=name)


class GameModelTest(TestCase):
    """
    Creates four games and checks if both is saved, games should be retrieved in ASC order
    """
    def test_save_and_retrieving_games(self):
        create_game(name='First game')
        create_game(name='Second game')
        create_game(name='Third game')
        create_game(name='Fourth game')

        saved_games = Game.objects.all()

        self.assertEqual(saved_games.count(), 4)
        self.assertEqual(saved_games[0].name, 'First game')
        self.assertEqual(saved_games[1].name, 'Fourth game')
        self.assertEqual(saved_games[2].name, 'Second game')
        self.assertEqual(saved_games[3].name, 'Third game')


def create_instruction(details, game):
    return Instruction.objects.create(details=details, game=game)


class InstructionModelTest(TestCase):
    """
    Creates two games and adds four connection instructions to them, ordered by datetime DESC, game name ASC
    """
    def test_save_and_retrieve_instructions(self):
        first_game = create_game('First game')
        second_game = create_game('Second game')

        instructions = [
            {'details': 'Instruction 1', 'game': first_game},
            {'details': 'Instruction 2', 'game': first_game},
            {'details': 'Instruction 3', 'game': second_game},
            {'details': 'Instruction 4', 'game': first_game},
        ]

        for i in instructions:
            create_instruction(details=i['details'], game=i['game'])
            sleep(0.01)

        saved_instructions = Instruction.objects.all()

        self.assertEqual(saved_instructions.count(), 4)
        self.assertEqual(saved_instructions[0].details, 'Instruction 4')
        self.assertEqual(saved_instructions[1].details, 'Instruction 3')
        self.assertEqual(saved_instructions[2].details, 'Instruction 2')
        self.assertEqual(saved_instructions[3].details, 'Instruction 1')