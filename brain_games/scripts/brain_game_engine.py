import prompt

from brain_games.cli import welcome_user


def run_game_engine(
    welcome_user, purpose_of_the_game, generate_question, calculate_correct_answer,
):
    """
    """
    username = welcome_user()
    print(purpose_of_the_game)  # noqa: WPS421
    for point in range(3):
        question = generate_question()
        correct_answer = calculate_correct_answer(question)
        print('Question: {0}'.format(question))  # noqa: WPS421
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')  # noqa: WPS421
        else:
            print(  # noqa: WPS421
                """'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!
                """.format(answer, correct_answer, username),
                )
            return None

    print('Congratulations, {0}!'.format(username))  # noqa: WPS421
