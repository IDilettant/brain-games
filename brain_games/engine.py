"""Template for running games."""
import prompt


def welcome_user():
    """Get an user name, greet player and return user name.

    Returns:
        Return username (str)

    """
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(username))
    return username


def run_game(game, rounds_number=3):
    """Run template for text game.

    Args:
        game:
            Provides access to functions that
            generate values unique for each game
        rounds_number (int):
            Number of rounds in the current game

    Returns:
        Return None.
    """
    username = welcome_user()
    print(game.DESCRIPTION)
    for _ in range(rounds_number):  # noqa: WPS122
        question, correct_answer = game.generate_round()
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                """'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!
                """.format(answer, correct_answer, username),
            )
            return

    print('Congratulations, {0}!'.format(username))
