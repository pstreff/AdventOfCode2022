

def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [line for line in f.read().splitlines()]


def part1(file='input_test.txt'):
    input = [tuple([
            set(line[:len(line)//2]),
            set(line[len(line)//2:])
        ]) for line in get_input(file)]

    priority = 0
    for compartment in input:
        shared_type = compartment[0] & compartment[1]  # set intersection
        # will also work with compartment[0].intersection(compartment[1])
        item = next(iter(shared_type))
        priority += ord(item) - (38 if item.isupper() else 96)
    print(priority)


def part2(file='input_test.txt'):
    input = get_input(file)
    priority = 0
    for i in range(0, len(input), 3):
        sets = [set(input[i+0]), set(input[i+1]), set(input[i+2])]
        shared_type = sets[0] & sets[1] & sets[2]

        item = next(iter(shared_type))
        priority += ord(item) - (38 if item.isupper() else 96)
    print(priority)


part1()
part1("input.txt")
part2()
part2("input.txt")
