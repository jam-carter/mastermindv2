def display_welcome_message():
    print("Welcome to Mastermind")
    print("The aim is to correctly guess the code generated by the computer, guess this code in 10 attempts and you win !")
    print("After each guess you will be told if you had the correct color in the correct position, or just the correct color\n")
    print("The colors are as follows: R (Red), G (Green), B (Blue, Y (Yellow), P (Purple), O (Orange)")
    print("The code will contain 4 of these colors, and they may be used more than once. Good luck !\n")

def get_user_guess(attempt):
    valid_colors = {'R', 'G', 'B', 'Y', 'P', 'O'}
    while True:
        guess = input(f"Attempt {attempt}: ").strip().upper().split()
        if len(guess) == 4 and all(color in valid_colors for color in guess):
            return guess
        else:
            print("Invalid input. Please enter 4 colors from the set {R, G, B, Y, P, O} separated by spaces.")

def display_feedback(correct_position, correct_number):
    print(f"Feedback: {correct_position} correct color(s) in the correct position, {correct_number} correct color(s) in the wrong position.")

def display_game_over_message(code):
    print(f"Sorry, you've used all attempts. The code was: {' '.join(code)}")
