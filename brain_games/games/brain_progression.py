#!/usr/bin/env python3
"""Arithmetic progression game."""
import random

from brain_games.cli import welcome_user
from brain_games.scripts.engine import run_game_engine

DESCRIPTION = 'What number is missing in the progression?'


def generate_question():  # noqa: WPS210
    """Generate arithmetic sequence with random skip.

    Returns:
        Return sequence (str)
    """
    number_size_limiter = 99
    sequence_size_limiter = 10
    start_number = random.randint(1, number_size_limiter)
    step_value = random. randint(1, sequence_size_limiter)
    position_in_sequence = random.randint(0, sequence_size_limiter - 1)
    sequence = [str(number) for number in range(
        start_number,
        start_number + sequence_size_limiter * step_value,
        step_value,
    )]
    sequence[position_in_sequence] = '..'
    return ' '.join(sequence)


def calculate_correct_answer(question):
    """Calculate the number missing in the arithmetic sequence.

    Args:
        question (str): arithmetic sequence

    Returns:
        Return number (int)
    """
    question = question.split()
    index_missing_number = question.index('..')
    question[index_missing_number] = 0
    question = [int(number) for number in question]
    for number in range(len(question)):  # noqa: WPS518
        if question[number] != 0 and question[number + 1] != 0:
            step_of_sequence = question[number + 1] - question[number]
            break
    if index_missing_number != 0:
        return str(question[index_missing_number - 1] + step_of_sequence)
    return str(question[index_missing_number + 1] - step_of_sequence)


def main():
    """Run main function."""
    run_game_engine(
        welcome_user,
        DESCRIPTION,
        generate_question,
        calculate_correct_answer,
    )


if __name__ == '__main__':
    main()
