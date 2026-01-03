import math
from py_compile import main
import numpy as np
import pandas as pd
from collections import defaultdict
import re

def compute_splits(puzzle):
    number_of_splits = 0

    number_of_lines = len(puzzle)

    for i in range(number_of_lines):

        line = puzzle[i]

        if i==0:
            s_position = line.index("S")
            # Add a beam below S unless there is a split
            if puzzle[i+1][s_position]!="^":
                puzzle[i+1] = puzzle[i+1][:s_position]+"|"+puzzle[i+1][s_position+1:]

        elif i>1 and i<number_of_lines-1:
            # Find all the beam positions in the previous line
            beam_positions = [i for i, letter in enumerate(puzzle[i-1]) if letter == "|"]

            # Find the split positions in the current line
            split_positions = [i for i, letter in enumerate(line) if letter == "^"]

            for pos in beam_positions:
                if pos not in split_positions:
                    puzzle[i] = puzzle[i][:pos]+"|"+puzzle[i][pos+1:]
                else:
                    number_of_splits += 1
                    puzzle[i+1] = puzzle[i+1][:pos-1]+"|"+puzzle[i+1][pos:pos+1]+"|"+puzzle[i+1][pos+2:]

        elif i==number_of_lines-1:
            # Find all the beam positions in the previous line
            beam_positions = [i for i, letter in enumerate(puzzle[i-1]) if letter == "|"]

            for pos in beam_positions:
                puzzle[i] = puzzle[i][:pos]+"|"+puzzle[i][pos+1:]


    return number_of_splits



def count_timelines(puzzle: list[str]) -> int:
    H = len(puzzle)
    W = len(puzzle[0])

    # find S (usually row 0)
    sr = next(r for r in range(H) if "S" in puzzle[r])
    sc = puzzle[sr].index("S")

    ways = defaultdict(int)
    ways[sc] = 1  # at row sr, col sc there is 1 timeline

    total = 0

    # propagate row by row
    for r in range(sr, H):
        next_ways = defaultdict(int)

        for c, cnt in ways.items():
            # if we're already on the last row, next "down" exits the manifold
            if r == H - 1:
                total += cnt
                continue

            below = puzzle[r + 1][c]

            if below == "^":
                # timeline splits: go to immediate left/right on the splitter row (r+1)
                for nc in (c - 1, c + 1):
                    if 0 <= nc < W:
                        next_ways[nc] += cnt
                    else:
                        # goes out of bounds -> exits
                        total += cnt
            else:
                # just fall straight down
                next_ways[c] += cnt

        ways = next_ways

    return total



def main():

    puzzle = []
    
    with open("/Users/matteotorba/Documents/GitHub/Advent_of_code_2025/Day 7/PuzzleInput", "r", encoding="utf-8") as f:
        for line in f:
            if line[0]!="*" and line[0]!="+":
                puzzle.append(line.rstrip("\n"))


            


    number_of_splits = compute_splits(puzzle)
    print(f"Total: {number_of_splits}")


    total_timelines = count_timelines(puzzle)
    print(f"Total timelines: {total_timelines}")
            


    

if __name__ == "__main__":
    main()