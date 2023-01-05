import math
import aocd
import numpy as np

SESH = "53616c7465645f5f3e5921a48d986bd7a6c0b32a89406ab714d51be3533e78fd0e493acde3d410900031ad585fb23841c340f3af4d8b1428062f04bfbbc555ad"

def get_input():
    return aocd.get_data(session=SESH, day=9, year=2022).splitlines()

def update_head(hx, hy, dir):
    if dir == "U":
        hy += 1
    elif dir == "D":
        hy -= 1
    elif dir == "L":
        hx -= 1
    else: # "R"
        hx += 1
    return hx, hy

def update_tail(hx, hy, tx, ty):
    for x in range(hx-1, hx+2):
        for y in range(hy-1, hy+2):
            if (x, y) == (tx, ty):
                return (tx, ty)

    if hx != tx and hy != ty:
        # diagonal movement
        if hx < tx and hy < ty:
            tx -= 1
            ty -= 1
        elif hx > tx and hy > ty:
            tx += 1
            ty += 1
        elif hx < tx and hy > ty:
            tx -= 1
            ty += 1
        else:
            tx += 1
            ty -= 1
    else:
        # x movement
        if (abs(hx - tx) > 1):
            if hx < tx:
                tx -= 1
            else:
                tx += 1
        # y movement
        if (abs(hy - ty) > 1):
            if hy < ty:
                ty -= 1
            else:
                ty += 1
    return tx, ty

def main():
    t_positions = set()
    (hx, hy), (tx, ty) = (0, 0), (0, 0)  #abolute position
    for line in get_input():
        dir = line[0]
        steps = int(line[2])
        for _ in range(steps):
            hx, hy = update_head(hx, hy, dir)
            tx, ty = update_tail(hx, hy, tx, ty)
            t_positions.add((tx, ty))
            
    print(len(t_positions))
        
if __name__ == "__main__":
    main() #3412 too low