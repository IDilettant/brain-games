#!/usr/bin/env python3
"""Arithmetic progression game."""
import random

DESCRIPTION = 'What number is missing in the progression?'
NUMBER_LIMITER = 99
SEQUENCE_LIMITER = 10


def generate_progression(start, length, step):
    """Generate arithmetic progression.

    Args:
        start (int): first number in sequence
        step (int): difference between adjacent numbers in a sequence
        length (int): number of elements in sequence

    Returns:
        Return arithmetic progression (list)
    """
    return list(range(start, start + length * step, step))


def generate_round():  # noqa: WPS210
    """Generate arithmetic sequence with random skip.

    Returns:
        Return sequence and value of scip (str)
    """
    start_number = random.randint(1, NUMBER_LIMITER)
    step_value = random. randint(1, NUMBER_LIMITER)
    sequence = [str(number) for number in generate_progression(
        start_number,
        SEQUENCE_LIMITER,
        step_value,
    )]
    missing_num_pos = random.randint(0, len(sequence) - 1)
    correct_answer = sequence[missing_num_pos]
    sequence[missing_num_pos] = '..'
    return ' '.join(sequence), correct_answer
