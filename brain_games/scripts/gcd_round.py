#!/usr/bin/env python3
"""Run brain-gcd game."""
from brain_games.games import brain_gcd
from brain_games.scripts.engine import run_engine


def main():
    """Run main function."""
    run_engine(brain_gcd)


if __name__ == '__main__':
    main()
