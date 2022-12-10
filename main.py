import os
from dotenv import load_dotenv
from day import AdventOfCodeDay

from importlib import import_module

for i in range(1, 10):
    import_module(f"day{i}")

if __name__ == "__main__":
    if not load_dotenv(override=True):
        raise ValueError("Could not find .env file")

    for aoc_day in AdventOfCodeDay.__subclasses__():
        day = aoc_day(session_key=os.environ["AOC_SESSION_KEY"])
        day.set_input_stream()

        print(day.solve_part_one())
        day.reset_input_stream()
        print(day.solve_part_two())
