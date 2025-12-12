import math
from py_compile import main
import numpy as np
import pandas as pd



def sum_invalid_IDS(ID_list):
    wrong_IDs = []
    wrong_IDs_sum = 0

    for ID in ID_list:
        print(ID)

        ID_splitted = ID.split('-')

        ID_vector = np.arange(int(ID_splitted[0]), int(ID_splitted[1]) + 1, 1)

        for number in ID_vector:
            digits = len(str(abs(number)))
            if digits % 2 == 0:
                first_half = str(number)[:digits//2]
                second_half = str(number)[digits//2:]

                if first_half == second_half:
                    print(f"Wrong ID found: {number}")
                    wrong_IDs.append(number)
                    wrong_IDs_sum += number

    return wrong_IDs_sum


def sum_invalid_IDS_2(ID_list):
    wrong_IDs = []
    wrong_IDs_sum = 0

    for ID in ID_list:
        print(ID)

        ID_splitted = ID.split('-')

        ID_vector = np.arange(int(ID_splitted[0]), int(ID_splitted[1]) + 1, 1)

        for number in ID_vector:
            digits = len(str(abs(number)))

            for i in range(1, digits//2 + 1):

                possible_repeater = (str(number)[:i])
                for j in range(i, digits, i):
                    next_segment = str(number)[j:j + i]
                    if possible_repeater != next_segment:
                        break
                else:
                    print(f"Wrong ID found: {number}")
                    wrong_IDs.append(number)
                    wrong_IDs_sum += number
                    break

    return wrong_IDs_sum






def main():

    ID_list = []
    
    with open("/Users/matteotorba/Documents/GitHub/Advent_of_code_2025/Day 2/PuzzleInput", "r", encoding="utf-8") as f:
        text = f.read()

    ID_list = [x.strip() for x in text.split(",") if x.strip()]
    print(ID_list)


    worng_IDS_sum = sum_invalid_IDS(ID_list)
    print(f"Wrong IDs sum: {worng_IDS_sum}")

    worng_IDS_sum_2 = sum_invalid_IDS_2(ID_list)
    print(f"Wrong IDs sum 2: {worng_IDS_sum_2}")

    

if __name__ == "__main__":
    main()