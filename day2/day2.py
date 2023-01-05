# ROCK <- A, X <- 1 <- BEATS: SCISSORS, BEATEN BY: PAPER
# PAPER <- B, Y <- 2 <- BEATS: ROCK, BEATEN BY: SCISSORS
# SCISSORS <- C, Z <- 3 <- BEATS: PAPER, BEATEN BY: ROCK
# WIN: 6, DRAW: 3, LOSE: 0
# X = LOSE, Y = DRAW, Z = WIN

def rps_score1():
    with open("/Users/ryan/Developer/AdventOfCode2022/day2/day2input.txt") as f:
        lines = f.readlines()

    score = 0

    for line in lines:
        round = line.split()
        opp = round[0]
        me = round[1]

        if me == 'X':
            score += 1
            if opp == 'A': score += 3
            elif opp == 'B': score += 0
            else: score += 6
        elif me == 'Y':
            score += 2
            if opp == 'A': score += 6
            elif opp == 'B': score += 3
            else: score += 0
        else:
            score += 3
            if opp == 'A': score += 0
            elif opp == 'B': score += 6
            else: score += 3

    return score

def rps_score2():
    with open("/Users/ryan/Developer/AdventOfCode2022/day2/day2input.txt") as f:
        lines = f.readlines()

    score = 0

    for line in lines:
        round = line.split()
        opp = round[0]
        outcome = round[1]

        if outcome == 'X': # I lose
            if opp == 'A': score += 3
            elif opp == 'B': score += 1
            else: score += 2
        elif outcome == 'Y': # I draw
            score += 3
            if opp == 'A': score += 1
            elif opp == 'B': score += 2
            else: score += 3
        else: # I win
            score += 6
            if opp == 'A': score += 2
            elif opp == 'B': score += 3
            else: score += 1

    return score

if __name__ == '__main__':
    print(rps_score1())
    print(rps_score2())