#!/usr/bin/env python3
"""Even-check game."""
import random

DESCRIPTION = (
    'Answer "yes" if the number is even, otherwise answer "no".'
)
NUMBER_LIMITER = 99


def is_even(num):
    """Determine if the number is even.

    Args:
        num (int): some number

    Returns:
        Return True or False (bool)
    """
    return num % 2 == 0


def generate_round():
    """Accumulates round-specific question and answer meanings.

    Returns:
        Returns calling a functions that
        returns of values question and answer
    """
    question = random.randint(1, NUMBER_LIMITER)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
