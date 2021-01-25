"""Template for running games."""
import prompt


def run_game_engine(welcome_user, purpose_of_the_game, generate_question, calculate_correct_answer):
    """Run template for text game.

    Args:
        welcome_user (function): Get an user name, greet player and return user name
        purpose_of_the_game (str): The description of the task for the game
        generate_question (function): Generate and return question for the game
        calculate_correct_answer (function): Calculate and return answer for actual game

    Returns:
        Return None.

    """
    username = welcome_user()
    print(purpose_of_the_game)
    for _point in range(3):  # noqa: WPS122
        question = generate_question()
        correct_answer = calculate_correct_answer(question)
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
