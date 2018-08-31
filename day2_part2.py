from functools import reduce

def calculate_division(row):
    numbers = [(x/y) if x%y is 0 and x is not y else 1 for x in row for y in row]
    result = int(reduce((lambda x, y: x*y), numbers))
    return(result)

if __name__ == '__main__':
    with open("day2_part2_input.txt") as f:
        lines = list(map(lambda x: list(map(int, x.split("\t"))), f.readlines()))
        result = reduce((lambda x,y: x+y), list(map(calculate_division, lines)))
        print(result)