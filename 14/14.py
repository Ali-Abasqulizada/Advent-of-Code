testcase = open('14/14.txt', 'r')

inputs = []

for line in testcase:
    line = line.split()
    col, row = line[0].split('=')[1].split(',')
    colAdd, rowAdd = line[1].split('=')[1].split(',')
    inputs.append((int(row), int(col), int(rowAdd), int(colAdd)))

matrix = [['.' for _ in range(101)] for _ in range(103)]

rows, cols = len(matrix), len(matrix[0])
middleR = rows // 2
middleC = cols // 2

def part1(i, j, di, dj, count):
    di *= count
    dj *= count
    di = -(abs(di) % rows) if di < 0 else di % rows
    dj = -(abs(dj) % cols) if dj < 0 else dj % cols
    i += di
    j += dj
    i = -(abs(i) % rows) if i < 0 else i % rows
    j = -(abs(j) % cols) if j < 0 else j % cols
    return i, j

for r, c, dr, dc in inputs:
    rr, cc = part1(r, c, dr, dc, 100)
    if matrix[rr][cc] == '.':
        matrix[rr][cc] = 1
    else:
        matrix[rr][cc] += 1

def find_quadrant(matrix):
    upLeft = 0
    upRight = 0
    downLeft = 0
    downRight = 0
    for r in range(middleR):
        for c in range(middleC):
            if matrix[r][c] != '.':
                upLeft += matrix[r][c]

    for r in range(middleR):
        for c in range(middleC + 1, cols):
            if matrix[r][c] != '.':
                upRight += matrix[r][c]

    for r in range(middleR + 1, rows):
        for c in range(middleC):
            if matrix[r][c] != '.':
                downLeft += matrix[r][c]

    for r in range(middleR + 1, rows):
        for c in range(middleC + 1, cols):
            if matrix[r][c] != '.':
                downRight += matrix[r][c]
    return upLeft * upRight * downLeft * downRight


def part2():
    result2 = 0
    min_ans2 = float('inf')
    for counter in range(10000):
        matrix = [['.' for _ in range(101)] for _ in range(103)]
        for r, c, dr, dc in inputs:
            rr, cc = part1(r, c, dr, dc, counter)
            if matrix[rr][cc] == '.':
                matrix[rr][cc] = 1
            else:
                matrix[rr][cc] += 1
        ans2 = find_quadrant(matrix)
        if ans2 < min_ans2:
            result2 = counter
            min_ans2 = ans2
    return result2

print(find_quadrant(matrix)) # 214400550
print(part2()) # 8149