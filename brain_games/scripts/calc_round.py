#!/usr/bin/env python3
"""Run brain-calc game."""
from brain_games.games import brain_calc
from brain_games.scripts.engine import run_engine


def main():
    """Run main function."""
    run_engine(brain_calc)


if __name__ == '__main__':
    main()
