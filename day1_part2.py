
def part_two(elements):
    elements = list(elements)
    half_elements_length = int(len(elements) / 2)
    result = 0
    for x in range(half_elements_length):
        if (elements[x] == elements[x+half_elements_length]):
            result = result + int(elements[x])
    return result * 2

if __name__ == '__main__':
    elements = "123425"
    result = part_two(elements)
    print(result)
