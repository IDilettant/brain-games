#!/usr/bin/env python3
"""Run brain-even game."""
from brain_games.engine import run_engine
from brain_games.games import brain_even


def main():
    """Run main function."""
    run_engine(brain_even)


if __name__ == '__main__':
    main()
