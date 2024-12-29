testcase = open('21/21.txt', 'r').read().split('\n')

numeric = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '#': (3, 0),
    '0': (3, 1),
    'A': (3, 2)
}

directional = {
    '#': (0, 0),
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
}

def find_numberic(robot1: str) -> list:
    result = []
    r, c = numeric['A']
    for ele in robot1:
        way = ''
        dr, dc = numeric[ele]
        row = abs(dr - r)
        col = abs(dc - c)
        way += 'v' * row if dr > r else '^' * row
        way += '>' * col if dc > c else '<' * col
        way += 'A'
        result.append(way)
        r, c = dr, dc
    return result

def find_directional(robots: list) -> list:
    result = []
    r, c = directional['A']
    for line in robots:
        way = ''
        for ele in line:
            dr, dc = directional[ele]
            row = abs(dr - r)
            col = abs(dc - c)
            way += 'v' * row if dr > r else '^' * row
            way += '>' * col if dc > c else '<' * col
            way += 'A'
            r, c = dr, dc
        result.append(way)
    return result

def find_ans(length: int, robot1: str) -> int:
    robot1 = int(robot1[:-1])
    print(length , robot1)
    return length * robot1

ans = 0

for robot1 in testcase:
    robot2 = find_numberic(robot1)
    print(robot2)
    robot3 = find_directional(robot2)
    me = find_directional(robot3)
    ans += find_ans(len(''.join(me)), robot1)

print(ans)


# ans = 0

# robot2 = find_numberic('379A')
# print(robot2)
# robot3 = find_directional(robot2)
# print(robot3)
# me = find_directional(robot3)
# print(me)
# ans += find_ans(len(''.join(me)), '379A')

# print(ans)