"""Command line interface for brain-games."""

import prompt


def welcome_user():
    """Get an user name, greet player and return user name.

    Returns:
        Return username (str)

    """
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(username))
    return username
