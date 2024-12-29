testcase = open('12/12.txt', 'r').read().split('\n')

matrix = []

for line in testcase:
    matrix.append(list(line))

rows, cols = len(matrix), len(matrix[0])

def part1(i: int, j: int, target: set) -> tuple[int]:
    p, a = 4, 1
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        rr, cc = i + dr, j + dc
        if 0 <= rr < rows and 0 <= cc < cols and matrix[rr][cc] == target:
            p -= 1
            if (rr, cc) not in visit:
                visit.add((rr, cc))
                per, are = part1(rr, cc, target)
                p += per
                a += are
    return p, a

def part2(i: int, j: int, target: str, region: set) -> int:
    a = 1
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        rr, cc = i + dr, j + dc
        if 0 <= rr < rows and 0 <= cc < cols and (rr, cc) not in visit and matrix[rr][cc] == target:
            visit.add((rr, cc))
            region.add((rr, cc))
            a += part2(rr, cc, target, region)
    return a


def part2_edges(plantRegion: set):
    pass


visit = set()
result = 0
result2 = 0

for r in range(rows):
    for c in range(cols):
        if (r, c) not in visit:
            visit.add((r, c))
            ele = matrix[r][c]
            p, a = part1(r, c, ele)
            result += p * a
            region = set()
            region.add((r, c))
            a2 = part2(r, c, ele, region)
            

print(result) # 1465112