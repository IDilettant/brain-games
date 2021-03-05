#!/usr/bin/env python3
"""Greatest common divisor game."""
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
NUMBER_LIMITER = 99


def generate_numbers():
    """Generate two random numbers.

    Returns:
        Return tuple with two numbers.
    """
    first_number = random.randint(1, NUMBER_LIMITER)
    second_number = random.randint(1, NUMBER_LIMITER)
    return first_number, second_number


def gcd(first_number, second_number):
    """Find the greatest common divisor of two numbers.

    Args:
        first_number (str): number
        second_number (str): number

    Returns:
        Return GCD (int)
    """
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


def generate_round():
    """Accumulates round-specific question and answer meanings.

    Returns:
        Returns calling a functions that
        returns of values question and answer
    """
    first_number, second_number = generate_numbers()
    correct_answer = str(gcd(first_number, second_number))
    question = '{0} {1}'.format(first_number, second_number)
    return question, correct_answer
