from collections import deque

testcase = open('18/18.txt', 'r').read().split('\n')

n = 71
till = 1024

matrix = [['.' for _ in range(n)] for _ in range(n)]

rows, cols = len(matrix), len(matrix[0])

def show_matrix(dumb: list[list]) -> None:
    for line in dumb:
        print(''.join(line))

for i in range(till):
    x, y = testcase[i].split(',')
    x, y = int(x), int(y)
    matrix[y][x] = '#'

def part1():
    stack = deque([(0, 0, 0)])
    visit = set()
    ans = float('inf')
    while stack:
        r, c, step = stack.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            rr, cc = r + dr, dc + c
            if 0 <= rr < rows and 0 <= cc < cols and (rr, cc) not in visit and matrix[rr][cc] != '#':
                if rr == rows - 1 and cc == cols - 1:
                    ans = min(ans, step + 1)
                    continue
                stack.append((rr, cc, step + 1))
                visit.add((rr, cc))  
    return ans

def part2(ways: list):
    for i in range(till, len(testcase)):
        print(ways)
        x, y = testcase[i].split(',')
        x, y = int(x), int(y)
        for j in range(len(ways)):
            if (y, x) in ways[j]:
                ways.pop(j)
        if len(ways) == 0:
            return (y, x)

best_step = part1()

print(best_step) # 384