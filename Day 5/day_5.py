import math
from py_compile import main
import numpy as np
import pandas as pd



def check_ingredient_in_sequence(sequences, ingredient):

    # Check if ingredient is in any of the sequences
    for seq in sequences:
        # Split the sequence into start and end
        seq_start = seq.split('-')[0]
        seq_end = seq.split('-')[1]
        # Check if ingredient is in the range
        if int(ingredient) >= int(seq_start) and int(ingredient) <= int(seq_end):
            return True
        
    return False


def check_all_ingredients(sequences, ingredients):

    fresh_ingredients = 0
    fresh_ingredients_list = []

    for ingredient in ingredients:
        if check_ingredient_in_sequence(sequences, ingredient) == True:
            fresh_ingredients +=1
            fresh_ingredients_list.append(ingredient)

    return fresh_ingredients


    return len(fresh_list), fresh_list

def count_fresh_ingredients(sequences):
    intervals = []
    for seq in sequences:
        a, b = seq.split("-", 1)
        intervals.append((int(a), int(b)))

    intervals.sort()
    merged = []
    for s, e in intervals:
        if not merged or s > merged[-1][1] + 1:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)

    return sum(e - s + 1 for s, e in merged)




def main():

    sequences = []
    ingredients = []
    empty_line_flag = False
    with open("/Users/matteotorba/Documents/GitHub/Advent_of_code_2025/Day 5/PuzzleInput", "r", encoding="utf-8") as f:
        for line in f:
            if line == "\n":
                empty_line_flag = True
                continue
            if not empty_line_flag:
                sequences.append(line.rstrip("\n"))
            else:
                ingredients.append(line.rstrip("\n"))
            

    # print(sequences)
    # print(ingredients)

    num_fresh_ingredients = check_all_ingredients(sequences, ingredients)
    print(f"Number of fresh ingredients: {num_fresh_ingredients}")

    count_fresh_ingredients_val = count_fresh_ingredients(sequences)
    print(f"Total fresh ingredients (method 2): {count_fresh_ingredients_val}")


    

if __name__ == "__main__":
    main()