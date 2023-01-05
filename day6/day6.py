import os

def parse_input():
    with open(os.path.join(os.path.dirname(__file__), 'day6.txt'), 'r') as f:
        return f.read()

def solution(input, n):
    for i in range(n, len(input)):
        if len(set(input[i-n:i])) == n:
            return(i)

if __name__ == '__main__':
    print(solution(parse_input(), 4))
    print(solution(parse_input(), 14))