testcase = open('6/6.txt', 'r').read().split('\n')

matrix = []

for line in testcase:
    matrix.append(list(line))

def show_matrix(dumb: list[list]) -> None:
    for line in dumb:
        print(''.join(line))

rows, cols = len(matrix), len(matrix[0])
directions = {
    '^': ('>', -1, 0),
    '>': ('v', 0, 1),
    'v': ('<', 1, 0),
    '<': ('^', 0, -1)
}
enemy = (None, None)

for r in range(rows):
    end = False
    for c in range(cols):
        if matrix[r][c] == '^':
            enemy = (r, c)
            end = True
            break
    if end:
        break

def part1() -> int:
    r, c = enemy
    matrix[r][c] = 'X'
    cross = 1
    direction = '^'
    couter = 0
    while True:
        couter += 1
        after, dr, dc = directions[direction]
        rr, cc = r + dr, c + dc
        if rr < 0 or rr >= rows or cc < 0 or cc >= cols:
            return cross
        elif matrix[rr][cc] == '#':
            direction = after
        else:
            if matrix[rr][cc] != 'X':
                matrix[rr][cc] = 'X'
                cross += 1
            r, c = rr, cc

print(part1()) # 5551