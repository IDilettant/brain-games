"""Command line interface for brain-games. Returns player name."""

import prompt


def welcome_user():
    """Get an user name, greet player and return user name."""  # noqa: DAR201
    print('Welcome to the Brain Games!')  # noqa: WPS421
    username = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(username))  # noqa: WPS421
    return username
