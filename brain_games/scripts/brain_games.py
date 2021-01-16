#!/usr/bin/env python3
"""Main programm."""

from brain_games.cli import welcome_user


def main():
    """Make a user intreface."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    welcome_user()


if __name__ == '__main__':
    main()
