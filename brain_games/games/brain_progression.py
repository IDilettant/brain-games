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


def generate_question():  # noqa: WPS210
    """Generate arithmetic sequence with random skip.45

    Returns:
        Return sequence (str)
    """
    number_size_limiter = 99
    sequence_size_limiter = 10
    start_number = random.randint(1, number_size_limiter)
    step_value = random. randint(1, sequence_size_limiter)
    missing_num_index = random.randint(0, sequence_size_limiter - 1)
    sequence = [str(number) for number in generate_progression(
        start_number,
        sequence_size_limiter,
        step_value,
    )]
    sequence[missing_num_index] = '..'
    return ' '.join(sequence)


def calculate_correct_answer(question):
    """Calculate the number missing in the arithmetic sequence.

    Args:
        question (str): arithmetic sequence

    Returns:
        Return number (int)
    """
    question = question.split()
    missing_num_index = question.index('..')
    question[missing_num_index] = 0
    question = [int(number) for number in question]
    for number in range(len(question)):  # noqa: WPS518
        if question[number] != 0 and question[number + 1] != 0:
            step_of_sequence = question[number + 1] - question[number]
            break
    if missing_num_index != 0:
        return str(question[missing_num_index - 1] + step_of_sequence)
    return str(question[missing_num_index + 1] - step_of_sequence)
