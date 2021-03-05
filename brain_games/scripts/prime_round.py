#!/usr/bin/env python3
"""Run brain-prime game."""
from brain_games.engine import run_game
from brain_games.games import brain_prime


def main():
    """Run main function."""
    run_game(brain_prime)


if __name__ == '__main__':
    main()
