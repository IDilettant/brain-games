#!/usr/bin/env python3
"""Run brain-calc game."""
from brain_games.engine import run_game
from brain_games.games import brain_calc


def main():
    """Run main function."""
    run_game(brain_calc)


if __name__ == '__main__':
    main()
