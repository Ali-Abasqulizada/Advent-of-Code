from collections import deque

testcase = open('16/16.txt', 'r').read().split('\n')

matrix = []

for line in testcase:
    matrix.append(list(line))

rows, cols = len(matrix), len(matrix[0])

def show_matrix(dumb: list[list]):
    for line in dumb:
        print(''.join(line))

start, end = None, None
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == 'S':
            start = r, c
        elif matrix[r][c] == 'E':
            end = r, c
        if start and end:
            break

def part1():
    r, c = start
    er, ec = end
    stack = deque([(r, c, 0, '>')])
    visit = {}
    visit[(r, c)] = float('inf')
    ans = float('inf')
    while stack:
        i, j, point, direction = stack.popleft()
        for dr, dc, n in [(0, 1, '>'), (-1, 0, '^'), (1, 0, 'v'), (0, -1, '<')]:
            rr, cc = i + dr, j + dc
            if 0 <= rr < rows and 0 <= cc < cols and matrix[rr][cc] !='#':
                newpoint = point + 1 if direction == n else point + 1001
                if rr == er and cc == ec:
                    ans = min(ans, newpoint)
                if (rr, cc) not in visit or newpoint < visit[(rr, cc)]:
                    visit[(rr, cc)] = newpoint
                    stack.append((rr, cc, newpoint, n))
    return ans

print(part1()) #130536