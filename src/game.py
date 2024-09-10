import random

def generate_code():
    colors = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'PURPLE', 'ORANGE']
    return [random.choice(colors) for _ in range(4)]

def get_feedback(guess, code):
    correct_position = sum([1 for i in range(4) if guess[i] == code[i]])
    correct_number = sum([min(guess.count(j), code.count(j)) for j in set(guess)]) - correct_position
    return correct_position, correct_number
