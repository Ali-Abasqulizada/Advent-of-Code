testcase = open('4/4.txt', 'r')

matrix = []

for line in testcase:
    matrix.append(line)
matrix[-1] += '\n'

ans = 0
for r in range(len(matrix)):
    for c in range(len(matrix[r]) - 1):
        if matrix[r][c] == 'X':
            if c - 3 >= 0 and matrix[r][c - 1] == 'M' and matrix[r][c - 2] == 'A' and matrix[r][c - 3] == 'S':
                ans += 1
            if r - 3 >= 0 and matrix[r - 1][c] == 'M' and matrix[r - 2][c] == 'A' and matrix[r - 3][c] == 'S':
                ans += 1
            if c + 3 < len(matrix[r]) - 1 and matrix[r][c + 1] == 'M' and matrix[r][c + 2] == 'A' and matrix[r][c + 3] == 'S':
                ans += 1
            if r + 3 < len(matrix) and matrix[r + 1][c] == 'M' and matrix[r + 2][c] == 'A' and matrix[r + 3][c] == 'S':
                ans += 1
            if r - 3 >= 0 and c - 3 >= 0 and matrix[r - 1][c - 1] == 'M' and matrix[r - 2][c - 2] == 'A' and matrix[r - 3][c - 3] == 'S':
                ans += 1
            if r - 3 >= 0 and c + 3 < len(matrix[r]) - 1 and matrix[r - 1][c + 1] == 'M' and matrix[r - 2][c + 2] == 'A' and matrix[r - 3][c + 3] == 'S':
                ans += 1
            if r + 3 < len(matrix) and c + 3 < len(matrix[r]) - 1 and matrix[r + 1][c + 1] == 'M' and matrix[r + 2][c + 2] == 'A' and matrix[r + 3][c + 3] == 'S':
                ans += 1
            if r + 3 < len(matrix) and  c - 3 >= 0 and matrix[r + 1][c - 1] == 'M' and matrix[r + 2][c - 2] == 'A' and matrix[r + 3][c - 3] == 'S':
                ans += 1

print(ans) # 2468

ans2 = 0

for r in range(len(matrix)):
    for c in range(len(matrix[r]) - 1):
        if matrix[r][c] == 'A':
            if r - 1 >= 0 and c - 1 >= 0 and r + 1 < len(matrix) and c + 1 < len(matrix[r]) - 1 and \
            ((matrix[r - 1][c - 1] == 'M' and matrix[r + 1][c + 1] == 'S') or (matrix[r + 1][c + 1] == 'M' and matrix[r - 1][c - 1] == 'S')) and \
            ((matrix[r - 1][c + 1] == 'M' and matrix[r + 1][c - 1] == 'S') or (matrix[r + 1][c - 1] == 'M' and matrix[r - 1][c + 1] == 'S')):
                ans2 += 1

print(ans2) # 1864