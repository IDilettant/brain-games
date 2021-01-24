#!/usr/bin/env python3
"""Greatest common divisor game."""
import random

from brain_games.cli import welcome_user
from brain_games.scripts.brain_game_engine import run_game_engine

PURPOSE_OF_THE_GAME = 'Find the greatest common divisor of given numbers.'


def generate_question():
    """.

    :return:
    """
    number_size_limiter = 99
    first_number = random.randint(1, number_size_limiter)  # noqa: S311
    second_number = random.randint(1, number_size_limiter)  # noqa: S311
    return '{0} {1}'.format(first_number, second_number)


def calculate_correct_answer(question):
    first_number, second_number = [int(number) for number in question.split()]
    while second_number != 0:
        first_number, second_number = (
            second_number, first_number % second_number,
        )
    return str(first_number)


def main():
    run_game_engine(welcome_user, purpose_of_the_game, generate_question, calculate_correct_answer)


if __name__ == '__main__':
    main()
