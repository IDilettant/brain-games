#!/usr/bin/env python3
"""Even-check game."""
import random

DESCRIPTION = (
    'Answer "yes" if the number is even, otherwise answer "no".'
)


def is_even(question):
    """Determine if the number is even.

    Args:
        question (int): some number

    Returns:
        Return True or False (bool)
    """
    if question % 2 == 0:
        return True
    return False


def calculate_correct_answer(question):
    """Check a number for even.

    Return 'yes' or 'no' depending on its parity

    Args:
        question (int): some number

    Returns:
        Return 'yes' or 'no' (str)
    """
    return 'yes' if is_even(question) else 'no'


def generate_round():
    """Accumulates round-specific question and answer meanings.

    Returns:
        Returns calling a functions that
        returns of values question and answer
    """
    number_size_limiter = 99
    question = random.randint(1, number_size_limiter)
    correct_answer = calculate_correct_answer(question)
    return question, correct_answer
