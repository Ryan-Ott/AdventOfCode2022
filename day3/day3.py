import os
import string
dirname = os.path.dirname(__file__)
day3 = os.path.join(dirname, 'day3.txt')
with open(day3) as f:
    lines = f.readlines()

# Part 1
def find_shared_types1():
    shared_types = []
    for line in lines:
        shared_types_in_bag = []
        line = line.strip()
        half = len(line) // 2
        first = line[:half]
        second = line[half:]
        for item in first:
            if item in second:
                if item not in shared_types_in_bag:
                    shared_types_in_bag.append(item)
                    shared_types.append(item)
    return shared_types
    
def find_priority_sum(shared_types):
    letters = string.ascii_letters
    priority_sum = 0
    for shared_type in shared_types:
        index = letters.index(shared_type)
        priority_sum += index + 1
    return priority_sum

# Part 2
def find_shared_types2():
    shared_types = []
    for i in range(0, len(lines), 3):
        bag1 = lines[i].strip()
        bag2 = lines[i+1].strip()
        bag3 = lines[i+2].strip()

        all_bags = [bag1, bag2, bag3]
        shortest_bag = min(all_bags, key=len)
        shared_types_in_bag = []
        
        for item in shortest_bag:
            if item in bag1 and item in bag2 and item in bag3:
                if item not in shared_types_in_bag:
                    shared_types_in_bag.append(item)
                    shared_types.append(item)
    return shared_types


if __name__ == '__main__':
    print(find_priority_sum(find_shared_types1()))
    print(find_priority_sum(find_shared_types2()))