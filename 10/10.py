testcase = open('10/10.txt', 'r').read().split('\n')

matrix = []

for line in testcase:
    matrix.append(list(line))

rows, cols = len(matrix), len(matrix[0])

def part1(i: int, j: int, nine_locations: set, visit: set) -> int:
    if matrix[i][j] == '9':
        if (i, j) not in nine_locations:
            nine_locations.add((i, j))
            return 1
        return 0
    elif (i, j) in visit:
        return 0
    visit.add((i, j))
    ans = 0
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        rr, cc = i + dr, j + dc
        if 0 <= rr < rows and 0 <= cc < cols and str(int(matrix[i][j]) + 1) == matrix[rr][cc]:
            ans += part1(rr, cc, nine_locations, visit)
    return ans

def part2(i: int, j: int, visit: set) -> int:
    if matrix[i][j] == '9':
        return 1
    visit.add((i, j))
    ans = 0
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        rr, cc = i + dr, j + dc
        if 0 <= rr < rows and 0 <= cc < cols and (rr, cc) not in visit and str(int(matrix[i][j]) + 1) == matrix[rr][cc]:
            visit.add((rr, cc))
            ans += part2(rr, cc, visit)
            visit.remove((rr, cc))
    return ans

result = 0
result2 = 0

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == '0':
            result += part1(r, c, set(), set())
            result2 += part2(r, c, set())

print(result) # 624
print(result2) # 1483