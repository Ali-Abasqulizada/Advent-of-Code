testcase = open('8/8.txt', 'r').read().split('\n')

matrix = []

for line in testcase:
    matrix.append(list(line))

rows, cols = len(matrix), len(matrix[0])

check = {}

for r in range(rows):
    for c in range(cols):
        ele = matrix[r][c]
        if ele == '.':
            continue
        if ele in check:
            check[ele].append((r, c))
        else:
            check[ele] = [(r, c)]

def part1(r1: int, c1: int, r2: int, c2: int) -> None:
    second_node_row = r2 - r1
    second_node_col = c2 - c1
    first_node_row = -second_node_row
    first_node_col = -second_node_col
    row1, col1 = r1 + first_node_row, c1 + first_node_col
    row2, col2 = r2 + second_node_row, c2 + second_node_col
    if 0 <= row1 < rows and 0 <= col1 < cols:
        antinodes.add((row1, col1))
    if 0 <= row2 < rows and 0 <= col2 < cols:
        antinodes.add((row2, col2))

def part2(r1: int, c1: int, r2: int, c2: int) -> None:
    antinodes2.add((r1, c1))
    antinodes2.add((r2, c2))
    second_node_row = r2 - r1
    second_node_col = c2 - c1
    first_node_row = -second_node_row
    first_node_col = -second_node_col
    row1, col1 = r1 + first_node_row, c1 + first_node_col
    row2, col2 = r2 + second_node_row, c2 + second_node_col
    while 0 <= row1 < rows and 0 <= col1 < cols:
        antinodes2.add((row1, col1))
        row1 += first_node_row
        col1 += first_node_col
    while 0 <= row2 < rows and 0 <= col2 < cols:
        antinodes2.add((row2, col2))
        row2 += second_node_row
        col2 += second_node_col

antinodes = set()
antinodes2 = set()

for ele in check:
    arr = check[ele]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            part1(arr[i][0], arr[i][1], arr[j][0], arr[j][1])
            part2(arr[i][0], arr[i][1], arr[j][0], arr[j][1])

print(len(antinodes)) # 291
print(len(antinodes2)) # 1015