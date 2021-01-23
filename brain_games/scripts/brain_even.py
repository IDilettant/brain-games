#!/usr/bin/env python
"""Even check game."""

import random

import prompt

from brain_games.cli import welcome_user


def ask_even_game(username):
    """Offer to player to determine the parity of random number.

    Up to three correct answers. Return None in case of wrong answer.
    """  # noqa: DAR101 DAR201
    correct_answer = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')  # noqa: WPS421
    while correct_answer < 3:
        # limit the value to two-digit number
        number = random.randint(1, 99)  # noqa: S311 WPS432
        print('Question: {0}'.format(number))  # noqa: WPS421
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and answer == 'yes' or number % 2 != 0 and answer == 'no':
            print('Correct!')  # noqa: WPS421
            correct_answer += 1
        else:
            if number % 2 == 0:  # noqa: WPS513
                print("'{0}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {1}!".format(answer, username))  # noqa: WPS421
                return None
            else:
                print("'{0}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {1}!".format(answer, username))  # noqa: WPS421
                return None

    print('Congratulations, {0}!'.format(username))  # noqa: WPS421


def main():
    """Start the even game."""
    ask_even_game(welcome_user())


if __name__ == '__main__':
    main()
