#!/usr/bin/env python3
"""Main programm."""

from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import ask_even_game


def main():
    """Make a user intreface."""
    welcome_user()


if __name__ == '__main__':
    main()
