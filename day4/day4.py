import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'day4.txt')

with open(filename) as f:
    lines = f.readlines()

def find_sections(line):
    ab = line.split(',')
    a = ab[0].split('-')
    b = ab[1].split('-')
    a_begin = int(a[0])
    a_end = int(a[1])
    sectionsA = range(a_begin, a_end + 1)

    b_begin = int(b[0])
    b_end = int(b[1])
    sectionsB = range(b_begin, b_end + 1)

    return sectionsA, sectionsB

def count_contains():
    count = 0
    for line in lines:
        a, b = find_sections(line)
        if set(a).issuperset(b) or set(b).issuperset(a):
            count += 1
    return count

def count_overlaps():
    count = 0
    for line in lines:
        a, b = find_sections(line)
        if set(a).intersection(b):
            count += 1
    return count

if __name__ == '__main__':
    print(count_contains())
    print(count_overlaps())