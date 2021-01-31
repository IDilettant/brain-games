#!/usr/bin/env python3
"""Prime number game."""
import random

DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def generate_question():
    """Generate a random number.

    Returns:
        Return number (int)
    """
    number_size_limiter = 99
    return random.randint(1, number_size_limiter)


def is_prime(question):
    """Determine if a number is prime.

    Args:
        question (int): some number

    Returns:
        Return True or False (bool)
    """
    if question == 2:
        return True
    if question % 2 == 0 or question < 2:
        return False
    for item in range(3, int(question ** 0.5) + 1, 2):  # noqa: WPS110
        if question % item == 0:
            return False
    return True


def calculate_correct_answer(question):
    """Check a number for prime.

    Return 'yes' or 'no' depending on result of checking

    Args:
        question (int): some number

    Returns:
        Return 'yes' or 'no' (str)
    """
    if is_prime(question):
        return 'yes'
    return 'no'
