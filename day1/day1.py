def max_calories():
    with open('/Users/ryan/Developer/AdventOfCode2022/day1/day1input.txt') as f:
        lines = f.readlines()

    elve = 0
    elve_calories = [0]
    for line in lines:
        if line == '\n':
            elve += 1
            elve_calories.append(0)
        else:
            elve_calories[elve] += int(line.strip())

    return max(elve_calories)

def top3_calories():
    with open('/Users/ryan/Developer/AdventOfCode2022/day1/day1input.txt') as f:
        lines = f.readlines()

    elve = 0
    elve_calories = [0]
    for line in lines:
        if line == '\n':
            elve += 1
            elve_calories.append(0)
        else:
            elve_calories[elve] += int(line.strip())

    elve_calories.sort(reverse=True)
    return sum(elve_calories[:3])

if __name__ == '__main__':
    print(max_calories())
    print(top3_calories())