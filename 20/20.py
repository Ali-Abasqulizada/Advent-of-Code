testcase = open('20/20.txt', 'r').read().split('\n')

matrix = []

for line in testcase:
    matrix.append(list(line))

rows, cols = len(matrix), len(matrix[0])
start, end = None, None

def show_matrix(dumb: list[list]) -> None:
    for line in dumb:
        print(''.join(line))

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == 'S':
            start = (r, c)
        elif matrix[r][c] == 'E':
            end = (r, c)
        if start and end:
            break
    
def find_track():
    r, c = start
    er, ec = end
    track = [(r, c, 0)]
    stack = [(r, c, 0, 0, 0)]
    last = None
    while stack:
        curr, curc, step, mover, movec = stack.pop()
        if curr == er and curc == ec:
            return track
        checkr, checkc = curr + mover, curc + movec
        if matrix[checkr][checkc] not in '#S':
            stack.append((checkr, checkc, step + 1, mover, movec))
            track.append((checkr, checkc, step + 1))
            last = track[-2][:-1]
            continue
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            rr, cc = curr + dr, curc + dc
            if matrix[rr][cc] != '#' and (rr, cc) != last:
                stack.append((rr, cc, step + 1, dr, dc))
                track.append((rr, cc, step + 1))
                last = track[-2][:-1]
                break

ways = find_track()

def part1(ways: list[list]) -> int:
    check = {}
    for i in range(len(ways)):
        sr, sc, s = ways[i]
        for j in range(i + 1, len(ways)):
            er, ec, e = ways[j]
            if (abs(er - sr) == 2 and ec == sc and matrix[(er + sr) // 2][ec] == '#') or \
               (abs(ec - sc) == 2 and er == sr and matrix[er][(ec + sc) // 2] == '#'):
                diff = e - s - 2
                check[diff] = check.get(diff, 0) + 1
    total = 0
    for key in check:
        if key >= 100:
            total += check[key]
    
    return total

def part2(ways: list[list]) -> int:
    check = {}
    for i in range(len(ways)):
        sr, sc, s = ways[i]
        for j in range(i + 1, len(ways)):
            er, ec, e = ways[j]
            diffr = abs(er - sr)
            diffc = abs(ec - sc)
            if (diffr + diffc <= 20):
                diff = e - s - (diffr + diffc)
                check[diff] = check.get(diff, 0) + 1
    total = 0
    for key in check:
        if key >= 100:
            total += check[key]
    
    return total

print(part1(ways)) # 1289
print(part2(ways)) # 982425