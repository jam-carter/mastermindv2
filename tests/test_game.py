import unittest
from game import generate_code, get_feedback

class TestGame(unittest.TestCase):

    def test_generate_code(self):
        code = generate_code()
        print("Generated code: ", code)
        self.assertEqual(len(code), 4)
        for color in code:
            self.assertIn(color.upper(),['RED', 'GREEN', 'BLUE', 'YELLOW', 'PURPLE', 'ORANGE'])

    def test_get_feedback(self):
        code = ['RED', 'GREEN', 'BLUE', 'YELLOW']
        guess = ['RED', 'BLUE', 'GREEN', 'PURPLE']
        feedback = get_feedback(guess, code)
        self.assertEqual(feedback[0], 1)
        self.assertEqual(feedback[1], 2)

if __name__ == '__main__':
    unittest.main()


