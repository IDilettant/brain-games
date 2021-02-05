#!/usr/bin/env python3
"""Calculate game."""
import operator
import random

DESCRIPTION = 'What is the result of the expression?'


def generate_question():
    """Generate a mathematical expression with two random terms.

    Returns:
        Return mathematical expression (str)
    """
    # limit the random number to two-digits for the convenience of the player
    number_size_limiter = 99
    first_number = random.randint(1, number_size_limiter)
    second_number = random.randint(1, number_size_limiter)
    math_operation_sign = random.choice(('+', '-', '*'))
    return '{0} {1} {2}'.format(
        first_number,
        math_operation_sign,
        second_number,
    )


def calculate_correct_answer(question):
    """Calculate a question and return answer.

    Args:
        question (str): mathematical expression

    Returns:
        Return the result of evaluating a mathematical expression (str)
    """
    question = question.split()
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    expr_result = operators[question[1]](
        int(question[0]),
        int(question[2]),
    )
    return str(expr_result)


def generate_round():
    """Accumulates round-specific question and answer meanings.

    Returns:
        Returns calling a functions that
        returns of values question and answer
    """
    question = generate_question()
    correct_answer = calculate_correct_answer(question)
    return question, correct_answer
