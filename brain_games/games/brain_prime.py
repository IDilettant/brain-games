#!/usr/bin/env python3
"""Prime number game."""
import random

DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)
NUMBER_LIMITER = 99


def is_prime(num):
    """Determine if a number is prime.

    Args:
        num (int): number

    Returns:
        Return True or False (bool)
    """
    if num == 2:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for item in range(3, int(num ** 0.5) + 1, 2):  # noqa: WPS110
        if num % item == 0:
            return False
    return True


def generate_round():
    """Accumulates round-specific question and answer meanings.

    Returns:
        Returns calling a functions that
        returns of values question and answer
    """
    question = random.randint(1, NUMBER_LIMITER)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
