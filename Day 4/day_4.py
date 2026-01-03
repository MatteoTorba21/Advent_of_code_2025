import math
from py_compile import main
import numpy as np
import pandas as pd

def is_roll_accessible(rolls, i, j):
    roll_height = len(rolls)
    roll_width = len(rolls[0])

    current_roll = rolls[i][j]

    number_of_other_rolls = 0

    # Check upwards
    if i>0:
        if rolls[i-1][j]=='@':
                number_of_other_rolls +=1
        if j>0:
            if rolls[i-1][j-1]=='@':
                number_of_other_rolls +=1   
        if j<roll_width-1:
            if rolls[i-1][j+1]=='@':
                number_of_other_rolls +=1

    # Check downwards
    if i<roll_height-1:
        if rolls[i+1][j]=='@':
            number_of_other_rolls +=1
        if j>0:
            if rolls[i+1][j-1]=='@':
                number_of_other_rolls +=1
        if j<roll_width-1:
            if rolls[i+1][j+1]=='@':
                number_of_other_rolls +=1

    # Check leftwards
    if j>0:
        if rolls[i][j-1]=='@':
            number_of_other_rolls +=1
   

    # Check rightwards
    if j<roll_width-1:
        if rolls[i][j+1]=='@':
            number_of_other_rolls +=1

    if number_of_other_rolls<4:
        return True
    else:
        return False


def get_accessible_rolls(rolls):
    num_accessible = 0
    positions = []
    for i, row in enumerate(rolls):
        
        for j in range(len(row)):
            if rolls[i][j]=='@':
                if is_roll_accessible(rolls, i, j) == True:
                    num_accessible += 1
                    positions.append((i,j))

    return num_accessible, positions

def remove_accessible_rolls_and_iterate(rolls):
    total_accessible = 0
    still_accessible = True

    while still_accessible:
        num_accessible, positions = get_accessible_rolls(rolls)
        total_accessible += num_accessible

        if num_accessible == 0:
            still_accessible = False
        else:
            for pos in positions:
                i, j = pos
                rolls[i] = rolls[i][:j] + '.' + rolls[i][j+1:]

    return total_accessible










def main():

    rolls = []
    with open("/Users/matteotorba/Documents/GitHub/Advent_of_code_2025/Day 4/PuzzleInput", "r", encoding="utf-8") as f:
        for line in f:
            rolls.append(line.rstrip("\n"))

    print(rolls)

    num_accessible_rolls, _ = get_accessible_rolls(rolls)
    print(f"Number of accessible rolls: {num_accessible_rolls}")

    num_accessible_rolls_iterated = remove_accessible_rolls_and_iterate(rolls)
    print(f"Number of accessible rolls after iterations: {num_accessible_rolls_iterated}")
   

    

    

if __name__ == "__main__":
    main()