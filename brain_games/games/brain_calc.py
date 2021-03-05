#!/usr/bin/env python3
"""Calculate game."""
import operator
import random

DESCRIPTION = 'What is the result of the expression?'
NUMBER_LIMITER = 99
operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}


def generate_expression():
    """Generate a mathematical expression with two random terms.

    Returns:
        Return tuple with elements of mathematical expression (str)
    """
    # limit the random number to two-digits for the convenience of the player
    first_number = random.randint(1, NUMBER_LIMITER)
    second_number = random.randint(1, NUMBER_LIMITER)
    operation = random.choice(list(operators.keys()))
    return (
        first_number,
        operation,
        second_number,
    )


def calculate_expression(frist_number, operation, second_number):
    """Calculate a question and return answer.

    Args:
        frist_number (str): number
        second_number (str): number
        operation (str): math operation sign

    Returns:
        Return the result of evaluating a mathematical expression (str)
    """
    return operators[operation](
        int(frist_number),
        int(second_number),
    )


def generate_round():
    """Accumulates round-specific question and answer meanings.

    Returns:
        Returns calling a functions that
        returns of values question and answer
    """
    frist_number, operation, second_number = generate_expression()
    correct_answer = str(calculate_expression(
        frist_number,
        operation,
        second_number,
    ))
    question = '{0} {1} {2}'.format(frist_number, operation, second_number)
    return question, correct_answer
