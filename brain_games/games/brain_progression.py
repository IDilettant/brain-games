#!/usr/bin/env python3
"""Arithmetic progression game."""
import random

DESCRIPTION = 'What number is missing in the progression?'


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
    number_size_limiter = 99
    sequence_size_limiter = 10
    start_number = random.randint(1, number_size_limiter)
    step_value = random. randint(1, sequence_size_limiter)
    missing_num_pos = random.randint(0, sequence_size_limiter - 1)
    sequence = [str(number) for number in generate_progression(
        start_number,
        sequence_size_limiter,
        step_value,
    )]
    correct_answer = sequence[missing_num_pos]
    sequence[missing_num_pos] = '..'
    return ' '.join(sequence), correct_answer
