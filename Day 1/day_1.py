import math
from py_compile import main
import numpy as np
import pandas as pd

def count_zeros_1(steps):
    pos = 50
    zero_count = 0

    for step in steps:

        if int(step[1:])>100:
            step = step[0] + str(int(step[1:]) % 100)

        if step[0] == "L":
            if pos - int(step[1:]) < 0:
                pos = 100 - (int(step[1:]) - pos)
            else:
                pos -= int(step[1:])
        elif step[0] == "R":
            if pos + int(step[1:]) >= 100:
                pos = (pos + int(step[1:])) - 100
            else:   
                pos += int(step[1:])

        if pos == 0:
            zero_count += 1

    return zero_count


def count_zeros_2(steps):
    pos = 50
    zero_count = 0

    for step in steps:

        if int(step[1:])>100:
            zero_count += math.floor(int(step[1:]) / 100)
            step = step[0] + str(int(step[1:]) % 100)

        if step[0] == "L":
            if pos - int(step[1:]) == 0:
                print("here")
            if pos - int(step[1:]) < 0:
                old_pos = pos
                pos = 100 - (int(step[1:]) - pos)
                if old_pos != 0:
                    zero_count += 1
            else:
                pos -= int(step[1:])

        elif step[0] == "R":
            if pos + int(step[1:]) == 100:
                print("here")
            if pos + int(step[1:]) > 100:
                pos = (pos + int(step[1:])) - 100
                zero_count += 1
            elif pos + int(step[1:]) == 100:
                pos = 0
            else:   
                pos += int(step[1:])

        if pos == 0:
            zero_count += 1

    return zero_count



def main():
    steps = []
    with open("/Users/matteotorba/Documents/GitHub/Advent_of_code_2025/Day 1/PuzzleInput", "r", encoding="utf-8") as f:
        for line in f:
            steps.append(line.rstrip("\n"))

    number_of_zeros = count_zeros_1(steps)
    print(f"Zero counts 1:{number_of_zeros}")

    number_of_zeros_2 = count_zeros_2(steps)
    print(f"Zero counts 2:{number_of_zeros_2}")


if __name__ == "__main__":
    main()



   