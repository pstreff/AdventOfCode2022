from collections import defaultdict


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [line for line in f.read().splitlines()]


def get_calories_list(input):
    elfs = defaultdict(int)
    index = 0
    for calories in input:
        if not calories:
            index += 1
            continue
        elfs[index] += int(calories)
    
    return elfs


def part1(file='input_test.txt'):
    input = get_input(file)
    elfs = get_calories_list(input)

    print(max(elfs.values()))


def part2(file='input_test.txt'):
    input = get_input(file)
    elfs = get_calories_list(input)

    top_three = sorted(elfs.values(), reverse=True)[:3]
    print(sum(top_three))


part1()
part1("input.txt")
part2()
part2("input.txt")
