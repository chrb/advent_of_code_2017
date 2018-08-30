import re
from functools import reduce

def calculate_difference(row):
    row = [int(x) for x in row]
    row.sort()
    return row[-1] - row[0]

if __name__ == '__main__':
    result = 0
    with open('day2_part1_input.txt') as f:
        lines = [x.split("\t") for x in f.read().splitlines()]
        #result = [calculate_difference(x) for x in lines]
        result = map(calculate_difference, lines)
        result = reduce((lambda x,y: x+y), result)
        print(result)
