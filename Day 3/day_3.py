import math
from py_compile import main
import numpy as np
import pandas as pd


def max_position(bank, max_val):
    positions = []
    for i, val in enumerate(bank):
        if val == max_val:
            positions.append(i)
    return positions



def bank_joltage(batteries_banks):

    sum_joltage = 0

    for bank in batteries_banks:
        max_digit = max((bank[:-1]))
        positions = max_position(bank, max_digit)

        max_voltage = 10*int(max_digit) + int(max(bank[positions[0]+1:]))

        sum_joltage += int(max_voltage)

    return sum_joltage



def bank_joltage_twelve(batteries_banks, bat_number):

    sum_joltage = 0

    bat_counter = np.arange(bat_number-1, -1, -1)

    for bank in batteries_banks:
        max_voltage = 0
        for i in bat_counter:

            if i!=0:
                max_digit = max((bank[:-i]))
            else:
                max_digit = max(bank)
            positions = max_position(bank, max_digit)

            bank = bank[positions[0]+1:]

            max_voltage += 10**i * int(max_digit)

        sum_joltage += int(max_voltage)

    return sum_joltage
    







def main():

    batteries_banks = []
    with open("/Users/matteotorba/Documents/GitHub/Advent_of_code_2025/Day 3/PuzzleInput", "r", encoding="utf-8") as f:
        for line in f:
            batteries_banks.append(line.rstrip("\n"))

    print(batteries_banks)


    total_joltage = bank_joltage(batteries_banks)
    print(f"Total joltage: {total_joltage}")

    total_joltage_twelve = bank_joltage_twelve(batteries_banks, 12)
    print(f"Total joltage for twelve batteries: {total_joltage_twelve}")

    

    

if __name__ == "__main__":
    main()