#!/usr/bin/env python3
"""Greatest common divisor game."""
import random

from brain_games.cli import welcome_user
from brain_games.scripts.engine import run_game_engine

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question():
    """Generate two random numbers.

    Returns:
        Return str with two numbers.
    """
    number_size_limiter = 99  # limit the random number to
    # two-digits for the convenience of the player
    first_number = random.randint(1, number_size_limiter)
    second_number = random.randint(1, number_size_limiter)
    return '{0} {1}'.format(first_number, second_number)


def calculate_correct_answer(question):
    """Find the greatest common divisor of two numbers.

    Args:
        question (str): two numbers

    Returns:
        Return GCD (str)
    """
    first_number, second_number = [int(number) for number in question.split()]
    while second_number != 0:
        first_number, second_number = (
            second_number, first_number % second_number,
        )
    return str(first_number)


def main():
    """Run main function."""
    run_game_engine(
        welcome_user,
        DESCRIPTION,
        generate_question,
        calculate_correct_answer,
    )


if __name__ == '__main__':
    main()
