testcase = open('25/25.txt', 'r').read().split('\n\n')

locks = []
keys = []

for line in testcase:
    matrix = line.split('\n')
    rows, cols = len(matrix), len(matrix[0])
    heights = []
    if matrix[0][0] == '#':
        for c in range(cols):
            height = -1
            for r in range(rows):
                if matrix[r][c] != '#':
                    break
                height += 1
            heights.append(height)
        locks.append(heights)
    else:
        for c in range(cols):
            height = -1
            for r in range(rows - 1, -1, -1):
                if matrix[r][c] != '#':
                    break
                height += 1
            heights.append(height)
        keys.append(heights)

def part1():
    ans = 0
    for lock in locks:
        for key in keys:
            fit = True
            for i in range(len(lock)):
                if lock[i] + key[i] > 5:
                    fit = False
            if fit:
                ans += 1
    return ans

print(part1()) # 3397