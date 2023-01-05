import os

def parse_input():
    with open(os.path.join(os.path.dirname(__file__), 'day5.txt'), 'r') as f:
        return f.read().splitlines()

def read_instruction(line):
    words = line.split() 
    count = int(words[1])
    origin = int(words[3])
    to = int(words[5])
    return count, origin, to

def read_stacks(stack_lines):
    stacks = [[], [], [], [], [], [], [], [], []]

    for i, line in enumerate(stack_lines):
        for j, char in enumerate(line):
            if char == '[' or char == ']' or char == ' ': continue
            stack = int((j - 1) / 4 + 1)
            stacks[stack-1].append(char)

    for i, stack in enumerate(stacks):
        stacks[i] = stack[::-1]
    return stacks

def part1():
    input = parse_input()
    stacks = read_stacks(input[:8])
    instructions = [read_instruction(line) for line in input[10:]]
    for count, origin, to in instructions:
        for _ in range(count):
            stacks[to-1].append(stacks[origin-1].pop())
    
    # return the concatenation of the top of each stack
    return ''.join([stack[-1] for stack in stacks])

def part2():
    input = parse_input()
    stacks = read_stacks(input[:8])
    instructions = [read_instruction(line) for line in input[10:]]
    for count, origin, to in instructions:
        crates_in_move = []
        for _ in range(count):
            crates_in_move.append(stacks[origin-1].pop())
        crates_in_move.reverse()
        for crate in crates_in_move:
            stacks[to-1].append(crate)
    
    # return the concatenation of the top of each stack
    return ''.join([stack[-1] for stack in stacks])

if __name__ == "__main__":
    print(part1())
    print(part2())