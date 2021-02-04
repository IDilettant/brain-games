"""Template for running games."""
import prompt

from brain_games.cli import welcome_user


def run_engine(game_modul):
    """Run template for text game.

    Args:
        game_modul:
            Provides access to functions that
            generate values unique for each game

    Returns:
        Return None.
    """
    username = welcome_user()
    print(game_modul.DESCRIPTION)
    for _point in range(3):  # noqa: WPS122
        question = game_modul.generate_question()
        correct_answer = game_modul.calculate_correct_answer(question)
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
            return None

    print('Congratulations, {0}!'.format(username))
