#!/usr/bin/env python3
"""Calculate game."""
import random

from brain_games.cli import welcome_user

from brain_games.scripts.brain_game_engine import run_game_engine


purpose_of_the_game = (
    'What is the result of the expression?'
    )


def generate_question():
    """Generate a question for the game."""
    # limit the random number to two-digits for the convenience of the player
    number_size_limiter = 99
    first_number = random.randint(1, number_size_limiter)  # noqa: S311
    second_number = random.randint(1, number_size_limiter)  # noqa: S311
    math_operation_sign = random.choice(('+', '-', '*'))  # noqa: S311
    return '{0} {1} {2}'.format(
        first_number, math_operation_sign, second_number,
    )


def calculate_correct_answer(question):
    """Calculate a question and return answer."""
    return str(eval(question))  # noqa: WPS421 S307


def main():
    run_game_engine(welcome_user, purpose_of_the_game, generate_question, calculate_correct_answer)


if __name__ == '__main__':
    main()
