import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import Game
from modules.Player import Player
from events.Events import MainEvents
import unittest
from unittest.mock import patch, MagicMock
import pygame


class TestGame(unittest.TestCase):
    def test_game_presence(self):
        game = Game(500, 500, "./media/Background.jpg")
        self.assertTrue(game)

class Testbarriers(unittest.TestCase):
    def test_barrier_health(self):
        game = Game(500, 500,"./media/Background.jpg")
        barrier = Barrier(
            x=25 + i * (75 + 50),  # start_x + i * (width + gap)
            y=self.h - 200,
            entity_img="./media/Barrier3.png",
            w=75,
            h=75,
            group=self.group,
            layer=1,
            score=None,
            health=3,
        ) 
        barrier.health -= 1
    self.assertEqual(barrier.health, 2)
    #barrier test
    

    


class TestPlayerMovement(unittest.TestCase):
    @patch("pygame.key.get_pressed")
    def test_left_key_movement(self, mock_get_pressed):

        # Fake keys: K_LEFT pressed, others False
        class FakeKeys:
            def __getitem__(self, key):
                return key == pygame.K_LEFT

        mock_get_pressed.return_value = FakeKeys()

        # Create a player and MainEvents
        player = Player(
            x=500 / 2 - 37.5,
            y=500 - 100,
            entity_img="./media/Boat.png",
            w=150,
            h=100,
            group=pygame.sprite.LayeredUpdates(),
            layer=1,
            score=None,
            health=3,
        )
        main_events = MainEvents(player, barriers=[], invaders=[], screen=None)

        player.velocity_x = 0  # ensure starting state
        main_events.player_key_handler()

        # Player should now be moving left
        self.assertEqual(player.velocity_x, -5)


# Source - https://stackoverflow.com/a
# Posted by Robert
# Retrieved 2025-12-08, License - CC BY-SA 3.0

if __name__ == "__main__":
    unittest.main(verbosity=2)




