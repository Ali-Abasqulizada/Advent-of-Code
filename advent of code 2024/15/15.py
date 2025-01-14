testcase = open('15/15.txt', 'r').read().split('\n')

matrix = []
moves = ''
finish_matrix = False
for line in testcase:
    if line == '':
        finish_matrix = True
        continue
    if not finish_matrix:
        matrix.append(list(line))
    else:
        moves += line

def show_matrix(dumb: list[list]) -> None:
    for line in dumb:
        print(''.join(line))

def calculateGPS(dumb: list[list]) -> int:
    ans = 0
    rows, cols = len(dumb), len(dumb[0])
    for r in range(rows):
        for c in range(cols):
            if dumb[r][c] == 'O' or dumb[r][c] == '[':
                ans += r * 100 + c
    return ans

def find_robot(dumb: list[list]) -> tuple[int, int]:
    rows, cols = len(dumb), len(dumb[0])
    row, col = None, None
    for r in range(rows):
        find_robot = False
        for c in range(cols):
            if dumb[r][c] == '@':
                row, col = r, c
                find_robot = True
                break
        if find_robot:
            break
    return row, col

def correct_matrix(dumb: list[tuple]) -> None:
    if dumb and len(dumb[0]) == 4:
        sorted_dumb = sorted(dumb, key=lambda x: x[3])
        for i, j, ele, counter in sorted_dumb:
            matrix2[i][j] = ele
    else:
        for i, j, ele in dumb:
            matrix2[i][j] = ele

matrix2 = []
def create_matrix2() -> None:
    rows, cols = len(matrix), len(matrix[0])
    for r in range(rows):
        one_row = []
        for c in range(cols):
            if matrix[r][c] == '#':
                one_row.extend(['#', '#'])
            elif matrix[r][c] == 'O':
                one_row.extend(['[', ']'])
            elif matrix[r][c] == '.':
                one_row.extend(['.', '.'])
            else:
                one_row.extend(['@', '.'])
        matrix2.append(one_row[::])

create_matrix2()
row1, col1 = find_robot(matrix)
row2, col2 = find_robot(matrix2)

def up(i: int, j: int) -> bool:
    if matrix[i][j] == '#':
        return False
    elif matrix[i][j] == 'O':
        if up(i - 1, j):
            matrix[i][j] = '.'
            matrix[i - 1][j] = 'O'
            return True
        else:
            return False
    return True

def right(i: int, j: int) -> bool:
    if matrix[i][j] == '#':
        return False
    elif matrix[i][j] == 'O':
        if right(i, j + 1):
            matrix[i][j] = '.'
            matrix[i][j + 1] = 'O'
            return True
        else:
            return False
    return True

def down(i: int, j: int) -> bool:
    if matrix[i][j] == '#':
        return False
    elif matrix[i][j] == 'O':
        if down(i + 1, j):
            matrix[i][j] = '.'
            matrix[i + 1][j] = 'O'
            return True
        else:
            return False
    return True

def left(i: int, j: int) -> bool:
    if matrix[i][j] == '#':
        return False
    elif matrix[i][j] == 'O':
        if left(i, j - 1):
            matrix[i][j] = '.'
            matrix[i][j - 1] = 'O'
            return True
        else:
            return False
    return True

def part1(row, col) -> None:
    for move in moves:
        if move == '^':
            if up(row - 1, col):
                matrix[row][col] = '.'
                matrix[row - 1][col] = '@'
                row -= 1
        elif move == '>':
            if right(row, col + 1):
                matrix[row][col] = '.'
                matrix[row][col + 1] = '@'
                col += 1
        elif move == 'v':
            if down(row + 1, col):
                matrix[row][col] = '.'
                matrix[row + 1][col] = '@'
                row += 1
        else:
            if left(row, col - 1):
                matrix[row][col] = '.'
                matrix[row][col - 1] = '@'
                col -= 1

def up2(i: int, j: int, exchange: list, counter: int) -> bool:
    if matrix2[i][j] == '#':
        return False
    elif matrix2[i][j] == '[':
        if up2(i - 1, j, exchange, counter - 1) and up2(i - 1, j + 1, exchange, counter - 1):
            exchange.extend([(i, j, '.', counter), (i, j + 1, '.', counter), (i - 1, j, '[', counter), (i - 1, j + 1, ']', counter)])
            return True
        else:
            return False
    elif matrix2[i][j] == ']':
        if up2(i - 1, j, exchange, counter - 1) and up2(i - 1, j - 1, exchange, counter - 1):
            exchange.extend([(i, j, '.', counter), (i, j - 1, '.', counter), (i - 1, j, ']', counter), (i - 1, j - 1, '[', counter)])
            return True
        else:
            return False
    return True

def right2(i: int, j: int, exchange: list) -> bool:
    if matrix2[i][j] == '#':
        return False
    elif matrix2[i][j] == '[':
        if right2(i, j + 2, exchange):
            exchange.extend([(i, j, '.'), (i, j + 1, '['), (i, j + 2, ']')])
            return True
        else:
            return False
    return True

def down2(i: int, j: int, exchange: list, counter: int) -> bool:
    if matrix2[i][j] == '#':
        return False
    elif matrix2[i][j] == '[':
        if down2(i + 1, j, exchange, counter - 1) and down2(i + 1, j + 1, exchange, counter - 1):
            exchange.extend([(i, j, '.', counter), (i, j + 1, '.', counter), (i + 1, j, '[', counter), (i + 1, j + 1, ']', counter)])
            return True
        else:
            return False
    elif matrix2[i][j] == ']':
        if down2(i + 1, j, exchange, counter - 1) and down2(i + 1, j - 1, exchange, counter - 1):
            exchange.extend([(i, j, '.', counter), (i, j - 1, '.', counter), (i + 1, j, ']', counter), (i + 1, j - 1, '[', counter)])
            return True
        else:
            return False
    return True

def left2(i: int, j: int, exchange: list) -> bool:
    if matrix2[i][j] == '#':
        return False
    elif matrix2[i][j] == ']':
        if left2(i, j - 2, exchange):
            exchange.extend([(i, j, '.'), (i, j - 1, ']'), (i, j - 2, '[')])
            return True
        else:
            return False
    return True

def part2(row, col) -> None:
    for move in moves:
        exchange = []
        if move == '^':
            if up2(row - 1, col, exchange, 0):
                correct_matrix(exchange)
                matrix2[row][col] = '.'
                matrix2[row - 1][col] = '@'
                row -= 1
        elif move == '>':
            if right2(row, col + 1, exchange):
                correct_matrix(exchange)
                matrix2[row][col] = '.'
                matrix2[row][col + 1] = '@'
                col += 1      
        elif move == 'v':
            if down2(row + 1, col, exchange, 0):
                correct_matrix(exchange)
                matrix2[row][col] = '.'
                matrix2[row + 1][col] = '@'
                row += 1                  
        else:
            if left2(row, col - 1, exchange):
                correct_matrix(exchange)
                matrix2[row][col] = '.'
                matrix2[row][col - 1] = '@'
                col -= 1

part2(row2, col2)
part1(row1, col1)
print(calculateGPS(matrix)) # 1437174
print(calculateGPS(matrix2)) # 1437468