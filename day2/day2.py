

part1_pattern = ["BX", "CY", "AZ", "AX", "BY", "CZ", "CX", "AY", "BZ"]
part2_pattern = ["BX", "CX", "AX", "AY", "BY", "CY", "CZ", "AZ", "BZ"]


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [line.replace(" ", "") for line in f.read().splitlines()]


def part1(file='input_test.txt'):
    input = get_input(file)
    score = 0
    for outcome in input:
        score += part1_pattern.index(outcome) + 1
    print(score)


def part2(file='input_test.txt'):
    input = get_input(file)
    score = 0
    for outcome in input:
        score += part2_pattern.index(outcome) + 1
    print(score)


part1()
part1("input.txt")
part2()
part2("input.txt")
