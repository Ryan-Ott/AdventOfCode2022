import aocd
from collections import defaultdict

AOC_SESSION = "53616c7465645f5f3e5921a48d986bd7a6c0b32a89406ab714d51be3533e78fd0e493acde3d410900031ad585fb23841c340f3af4d8b1428062f04bfbbc555ad"

def get_sizes():
    lines = aocd.get_data(session=AOC_SESSION, year=2022, day=7).splitlines()
    lines = [line for line in lines if line != "$ ls"]
    filepath = []
    sizes = defaultdict(int)

    for line in lines:
        if line.startswith("$ cd"):
            match line:
                case "$ cd /":
                    filepath.clear()
                    filepath.append("/")
                case "$ cd ..":
                    filepath.pop()
                case _:
                    dir = line.split()[-1]
                    filepath.append(dir)
        else:
            filesize = line.split()[0]
            if filesize.isdigit():
                filesize = int(filesize)
                for i in range(len(filepath)):
                    dir = '/'.join(filepath[:i+1]).replace("//", "/")
                    sizes[dir] += filesize
    return sizes

def main():
    sizes = get_sizes()
    # Find the sum of all directories with a size less than or equal to 100000
    dirs_below_threshold = {directory: size for (directory, size) in sizes.items() if size <= 100000}
    print(sum(dirs_below_threshold.values()))

    total_space = 70000000
    needed_space = 30000000
    space_to_free = sizes["/"] + needed_space - total_space
    dirs_above_threshold = {directory: size for (directory, size) in sizes.items() if size >= space_to_free}
    print(min(dirs_above_threshold.values()))

if __name__ == "__main__":
    main()
