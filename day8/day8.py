import aocd

SESH = "53616c7465645f5f3e5921a48d986bd7a6c0b32a89406ab714d51be3533e78fd0e493acde3d410900031ad585fb23841c340f3af4d8b1428062f04bfbbc555ad"

def get_grid():
    lines = aocd.get_data(session=SESH, year=2022, day=8).splitlines()
    grid = []
    for line in lines:
        grid.append([int(x) for x in line])
    return grid

def count_visible(grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if col == 0 or col == len(grid[row]) - 1 or row == 0 or row == len(grid) - 1:
                count += 1
            else:
                invis_count = 0
                for y in range(0, row):  # above
                    if grid[y][col] >= grid[row][col]:
                        invis_count += 1
                        break
                for y in range(row + 1, len(grid)):  # below
                    if grid[y][col] >= grid[row][col]:
                        invis_count += 1
                        break
                for x in range(0, col):  # left
                    if grid[row][x] >= grid[row][col]:
                        invis_count += 1
                        break
                for x in range(col + 1, len(grid[row])):  # right
                    if grid[row][x] >= grid[row][col]:
                        invis_count += 1
                        break
                if invis_count < 4:
                    count += 1
    return(count)

def max_scenic_score(grid):
    max = 0
    for row in range(0, len(grid)):
        for col in range(len(grid[row])):
            if col == 0 or col == len(grid[row]) - 1 or row == 0 or row == len(grid) - 1:
                continue
            viewing_distance, vd_a, vd_b, vd_l, vd_r = 0, 0, 0, 0, 0
            for y in range(row-1, -1, -1):  # above
                vd_a += 1
                if grid[y][col] >= grid[row][col]: break
            for y in range(row + 1, len(grid)):  # below
                vd_b += 1
                if grid[y][col] >= grid[row][col]: break
            for x in range(col-1, -1, -1):  # left
                vd_l += 1
                if grid[row][x] >= grid[row][col]: break
            for x in range(col + 1, len(grid[row])):  # right
                vd_r += 1
                if grid[row][x] >= grid[row][col]: break
            viewing_distance = vd_a * vd_b * vd_l * vd_r
            if viewing_distance > max:
                max = viewing_distance
    return max

if __name__ == '__main__':
    print(count_visible(get_grid()))
    print(max_scenic_score(get_grid()))  # 389376 is too high