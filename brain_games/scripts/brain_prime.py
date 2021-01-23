#!/usr/bin/env python3
"""Prime number game."""
import random

from brain_games.cli import welcome_user
from brain_games.scripts.brain_game_engine import run_game_engine

purpose_of_the_game = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
    )


def generate_question():
    number_size_limiter = 99  # noqa: WPS311
    return random.randint(1, number_size_limiter)


def calculate_correct_answer(question):
    def is_prime(number):
        if number == 2:
            return True
        if number % 2 == 0 or number < 2:
            return False
        for item in range(3, int(number ** 0.5) + 1, 2):  # noqa: WPS110
            if number % item == 0:
                return False
        return True

    if is_prime(int(question)):
        return 'yes'
    return 'no'


def main():
    """."""
    run_game_engine(welcome_user, purpose_of_the_game, generate_question, calculate_correct_answer)


if __name__ == '__main__':
    main()
