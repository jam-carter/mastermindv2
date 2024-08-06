def main():
    import game
    import interface

    code = game.generate_code()
    attempts = 10

    interface.display_welcome_message()

    for attempt in range(1, attempts + 1):
        guess = interface.get_user_guess(attempt)
        correct_position, correct_number = game.get_feedback(guess, code)
        interface.display_feedback(correct_position, correct_number)

        if correct_position == 4:
            print("Congratulations! You've guessed the code!")
            break
    else:
        interface.display_game_over_message(code)


if __name__ == "__main__":
    main()
