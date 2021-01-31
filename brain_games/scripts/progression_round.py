#!/usr/bin/env python3
"""Run brain-progression game."""
from brain_games.games import brain_progression
from brain_games.scripts.engine import run_engine


def main():
    """Run main function."""
    run_engine(brain_progression)


if __name__ == '__main__':
    main()
