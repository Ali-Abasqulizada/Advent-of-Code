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

def loop(r: int, c: int) -> int:
    original = matrix[r][c]
    matrix[r][c] = '#'
    seen = set()
    direction = '^'
    i, j = enemy
    while True:
        if (i, j, direction) in seen:
            matrix[r][c] = original
            return True

        seen.add((i, j, direction))
        after, dr, dc = directions[direction]
        rr, cc = i + dr, j + dc

        if rr < 0 or rr >= rows or cc < 0 or cc >= cols:
            matrix[r][c] = original
            return False
        elif matrix[rr][cc] == '#':
            direction = after
        else:
            i, j = rr, cc

def part1() -> int:
    r, c = enemy
    matrix[r][c] = 'X'
    cross = 1
    direction = '^'
    while True:
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

def part2() -> int:
    count = 0
    for r in range(rows):
        print(r)
        for c in range(cols):
            if matrix[r][c] not in '#^':
                if loop(r, c):
                    count += 1
    return count

print(part1()) # 5551
print(part2()) # 1939