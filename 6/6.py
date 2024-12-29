testcase = open('6/6.txt', 'r')

matrix = []

for line in testcase:
    matrix.append(list(line))

matrix[-1] += '\n'

r, c = 0, 0

for i in range(len(matrix)):
    finish = False
    for j in range(len(matrix[i])):
        if matrix[i][j] == '^':
            r, c = i, j
            finish = True
            break
    if finish:
        break

cross = 1
matrix[r][c] = 'X'
starting = r, c
up = True
left = False
right = False
down = False
end = False

while True:
    while up:
        if r == 0:
            end = True
            break
        elif matrix[r - 1][c] == '#':
            up = False
            right = True
            break
        else:
            r -= 1
            if matrix[r][c] != 'X':
                cross += 1
                matrix[r][c] = 'X'
    while right:
        if c == len(matrix[r]) - 2:
            end = True
            break
        elif matrix[r][c + 1] == '#':
            right = False
            down = True
            break
        else:
            c += 1
            if matrix[r][c] != 'X':
                cross += 1
                matrix[r][c] = 'X'
    while down:
        if r == len(matrix) - 1:
            end = True
            break
        elif matrix[r + 1][c] == '#':
            down = False
            left = True
            break
        else:
            r += 1
            if matrix[r][c] != 'X':
                cross += 1
                matrix[r][c] = 'X'
    while left:
        if c == 0:
            end = True
            break
        elif matrix[r][c - 1] == '#':
            left = False
            up = True
            break
        else:
            c -= 1
            if matrix[r][c] != 'X':
                cross += 1
                matrix[r][c] = 'X'
    if end:
        break

print(cross) # 5551