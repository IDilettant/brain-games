#!/usr/bin/env python3
"""Run brain-progression game."""
from brain_games.engine import run_engine
from brain_games.games import brain_progression


def main():
    """Run main function."""
    run_engine(brain_progression)


if __name__ == '__main__':
    main()
