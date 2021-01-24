#!/usr/bin/env python3
"""Arithmetic progression game."""
import random

from brain_games.cli import welcome_user
from brain_games.scripts.brain_game_engine import run_game_engine

PURPOSE_OF_THE_GAME = (
    'What number is missing in the progression?'
    )


def generate_question():
    """."""
    number_size_limiter = 99
    sequence_size_limiter = 10
    start_number = random.randint(1, number_size_limiter)  # noqa: S311
    step_value = random. randint(1, sequence_size_limiter)  # noqa: S311
    position_in_sequence = random.randint(1, sequence_size_limiter)  # noqa: S311
    sequence = [str(number) for number in range(start_number, start_number + sequence_size_limiter * step_value, step_value)]
    sequence[position_in_sequence] = '..'
    question = ' '.join(sequence)
    return question


def calculate_correct_answer(question):
    """."""
    question = question.split()
    index_missing_number = question.index('..')
    question[index_missing_number] = 0
    question = [int(number) for number in question]
    for number in range(len(question)):
        if question[number] != 0 and question[number + 1] != 0:
            step_of_sequence = question[number + 1] - question[number]
            break
    if index_missing_number != 0:
        return str(question[index_missing_number - 1] + step_of_sequence)
    else:
        return str(question[index_missing_number + 1] - step_of_sequence) 


def main():
    """."""
    run_game_engine(welcome_user, purpose_of_the_game, generate_question, calculate_correct_answer)


if __name__ == '__main__':
    main()
