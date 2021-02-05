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
    if is_even(question):
        return 'yes'
    return 'no'


def generate_round():
    """Accumulates round-specific question and answer meanings.

    Returns:
        Returns calling a functions that
        returns of values question and answer
    """
    question = generate_question()
    correct_answer = calculate_correct_answer(question)
    return question, correct_answer
