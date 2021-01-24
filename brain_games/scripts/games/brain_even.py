#!/usr/bin/env python3
"""Even-check game."""
import random

from brain_games.cli import welcome_user
from brain_games.scripts.brain_game_engine import run_game_engine

purpose_of_the_game = (
    'Answer "yes" if the number is even, otherwise answer "no".'
    )


def generate_question():
    """Return a question for the game."""
    # limit the random number to two-digits for the convenience of the player
    number_size_limiter = 99
    return random.randint(1, number_size_limiter)  # noqa: S311


def calculate_correct_answer(question):
    if question % 2 == 0:
        return 'yes'
    return 'no'


def main():
    run_game_engine(welcome_user, purpose_of_the_game, generate_question, calculate_correct_answer)


if __name__ == '__main__':
    main()

