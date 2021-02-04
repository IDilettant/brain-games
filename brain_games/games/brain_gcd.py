#!/usr/bin/env python3
"""Greatest common divisor game."""
import random

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


def gcd(question):
    """Find the greatest common divisor of two numbers.

    Args:
        question (str): two numbers

    Returns:
        Return GCD (int)
    """
    first_number, second_number = [int(number) for number in question.split()]
    while second_number != 0:
        first_number, second_number = (
            second_number, first_number % second_number,
        )
    return first_number


def calculate_correct_answer(question):
    """Convert found greatest common divisor of two numbers to string.

    Args:
        question (str): two numbers

    Returns:
        Return GCD (str)
    """
    return str(gcd(question))
