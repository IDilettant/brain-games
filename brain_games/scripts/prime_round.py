#!/usr/bin/env python3
"""Run brain-prime game."""
from brain_games.engine import run_engine
from brain_games.games import brain_prime


def main():
    """Run main function."""
    run_engine(brain_prime)


if __name__ == '__main__':
    main()
