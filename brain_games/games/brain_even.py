#!/usr/bin/env python3
"""Even-check game."""
import random

DESCRIPTION = (
    'Answer "yes" if the number is even, otherwise answer "no".'
)


def generate_question():
    """Generate a random number.

    Returns:
        Return number (int)
    """
    # limit the random number to two-digits for the convenience of the player
    number_size_limiter = 99
    return random.randint(1, number_size_limiter)


def calculate_correct_answer(question):
    """Determine if the number is even.

    Args:
        question (int): some number

    Returns:
        Return 'yes' or 'no' (str)
    """
    if question % 2 == 0:
        return 'yes'
    return 'no'
