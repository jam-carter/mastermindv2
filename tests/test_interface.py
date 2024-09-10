import unittest
from unittest.mock import patch
from interface import get_user_guess, display_welcome_message, display_feedback, display_game_over_message

class TestInterface(unittest.TestCase):

    @patch('builtins.input', return_value='RED GREEN BLUE YELLOW')
    def test_get_user_guess(self, mock_input):
        guess = get_user_guess(1)
        self.assertEqual(guess, ['RED', 'GREEN', 'BLUE', 'YELLOW'])

    def test_display_welcome_message(self):
        with patch('builtins.print') as mock_print:
            display_welcome_message()
            mock_print.assert_called()
            # Add specific checks for exact print statements if needed

    def test_display_feedback(self):
        with patch('builtins.print') as mock_print:
            display_feedback(2, 1)
            mock_print.assert_called_with("Feedback: 2 correct color(s) in the correct position, 1 correct color(s) in the wrong position.")

    def test_display_game_over_message(self):
        with patch('builtins.print') as mock_print:
            display_game_over_message(['RED', 'GREEN', 'BLUE', 'YELLOW'])
            mock_print.assert_called_with("Sorry, you've used all attempts. The code was: RED GREEN BLUE YELLOW")

if __name__ == '__main__':
    unittest.main()
