import math
from py_compile import main
import numpy as np
import pandas as pd
import re

def numbers_with_spaces(line: str) -> list[str]:
    s = line.rstrip("\n")  # keep trailing spaces, drop only newline
    matches = list(re.finditer(r'(-?\d+)(\s*)', s))

    out = []
    for i, m in enumerate(matches):
        num = m.group(1)
        ws  = m.group(2)

        # if there's another number after this one, drop exactly 1 whitespace char
        if i < len(matches) - 1 and ws:
            ws = ws[1:]

        out.append(num + ws)

    return out

import re

def tokens_num_plus_spaces(line: str) -> list[str]:
    s = line.rstrip("\n")  # keep trailing spaces, drop only newline

    matches = list(re.finditer(r'-?\d+', s))
    if not matches:
        return []

    out = []
    leading_ws = s[:matches[0].start()]  # spaces before the first number (if any)

    for i, m in enumerate(matches):
        num = m.group()
        end = m.end()
        next_start = matches[i + 1].start() if i < len(matches) - 1 else len(s)

        gap = s[end:next_start]  # whitespace after this number (or trailing whitespace)
        if i < len(matches) - 1 and gap:   # drop exactly one delimiter whitespace
            gap = gap[1:]

        token = num + gap
        if i == 0 and leading_ws:          # preserve spaces before the first number
            token = leading_ws + token

        out.append(token)

    return out




def compute_total(numbers, operations):
    total = 0
    for i, oper in enumerate(operations):
        if oper == '*':
            prod = 1
            for j in range(len(numbers)):
                prod *= numbers[j][i]
            total += prod

        elif oper == '+':
            for j in range(len(numbers)):
                total += numbers[j][i]
            

    return total

def compute_total_vertical(numbers, operations):
    total = 0

    oeprations_reversed = operations[::-1]

    for i, oper in enumerate(oeprations_reversed):

        numbers_column = []

        for k in range(len(numbers[0])):
            k +=1
            if k>1 and numbers[0][-k:-k+1] == " " and numbers[1][-k:-k+1] == " " and numbers[2][-k:-k+1] == " " and numbers[3][-k:-k+1] == " ":
                numbers[0] = numbers[0][:-k]
                numbers[1] = numbers[1][:-k]
                numbers[2] = numbers[2][:-k]
                numbers[3] = numbers[3][:-k]
                break
            else:
                if k>1:
                    num = numbers[0][-k:-k+1] + numbers[1][-k:-k+1] + numbers[2][-k:-k+1] + numbers[3][-k:-k+1]
                else:
                    num = numbers[0][-k:] + numbers[1][-k:] + numbers[2][-k:] + numbers[3][-k:]


                numbers_column.append(int(num))


        if oper == '*':
            prod = 1
            for j in range(len(numbers_column)):
                prod *= numbers_column[j]
            total += prod

        elif oper == '+':
            for j in range(len(numbers_column)):
                total += numbers_column[j]
            

    return total




def compute_total_vertical_2(numbers, operations):
    total = 0

    oeprations_reversed = operations[::-1]

    for i, oper in enumerate(oeprations_reversed):

        numbers_column = []
        # iterate from the END to the beginning of each line of text until in all the lines there is a space


        for k in range(len(numbers[0])):
            k +=1
            if k>1 and numbers[0][-k:-k+1] == " " and numbers[1][-k:-k+1] == " " and numbers[2][-k:-k+1] == " ":
                numbers[0] = numbers[0][:-k]
                numbers[1] = numbers[1][:-k]
                numbers[2] = numbers[2][:-k]
                break
            else:
                if k>1:
                    num = numbers[0][-k:-k+1] + numbers[1][-k:-k+1] + numbers[2][-k:-k+1]
                else:
                    num = numbers[0][-k:] + numbers[1][-k:] + numbers[2][-k:]


                numbers_column.append(int(num))


        if oper == '*':
            prod = 1
            for j in range(len(numbers_column)):
                prod *= numbers_column[j]
            total += prod

        elif oper == '+':
            for j in range(len(numbers_column)):
                total += numbers_column[j]
            

    return total




def main():

    numbers = []
    numbers_strings = []
    operations = ""
    with open("/Users/matteotorba/Documents/GitHub/Advent_of_code_2025/Day 6/PuzzleInput", "r", encoding="utf-8") as f:
        for line in f:
            if line[0]!="*" and line[0]!="+":
                numbers_new = [int(e) for e in line.split()]
                numbers.append(numbers_new)

                numbers_strings.append(line.rstrip("\n"))

            else:
                operations = [e for e in line.split()]

            


    total = compute_total(numbers, operations)
    print(f"Total: {total}")

    total_vertical = compute_total_vertical(numbers_strings, operations)
    print(f"Total vertical: {total_vertical}")


            


    

if __name__ == "__main__":
    main()