import unittest
from unittest.mock import patch
from io import StringIO
from text_game import Player, print_pause, read_zonemap, player_move, prompt, player_kind, help_menu

class TestTextGame(unittest.TestCase):

    def setUp(self):
        self.player = Player(name="Player", hp=2)

    def test_player(self):
        self.assertEqual(self.player.name, "Player")
        self.assertEqual(self.player.hp, 2)
        self.assertEqual(self.player.location, "Entrance")

    def test_print_pause(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print_pause("test")
        self.assertEqual(fake_output.getvalue().strip(), "test")

    def test_read_zonemap(self):
        zonemap = read_zonemap('zonemap.txt')
        self.assertIsInstance(zonemap, dict)

                
    def test_player_move(self):
        zonemap = read_zonemap('zonemap.txt')
        player_move(zonemap, self.player, 'Left')
        self.assertEqual(self.player.location, "Bedroom")
        player_move(zonemap, self.player, 'Up')
        self.assertEqual(self.player.location, "Wardrobe")
        player_move(zonemap, self.player, 'Leave')
        self.assertEqual(self.player.location, "Bedroom")
        with self.assertRaises(KeyError):
            player_move(zonemap, self.player, 'Down')

if __name__ == '__main__':
    unittest.main()
