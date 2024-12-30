conditions, equations = open('24/24.txt', 'r').read().split('\n\n')

check = {}
check2 = {}
marks = []
z = []

for codition in conditions.split('\n'):
    key, mark = codition.split(': ')
    check[key] = int(mark)

for equation in equations.split('\n'):
    aopeb, c = equation.split(' -> ')
    a, ope, b = aopeb.split(' ')
    check2[c] = (a, ope, b)
    marks.append(c)
    if c[0] == 'z':
        z.append(c)

z.sort(reverse=True)

def part1(marks):
    while marks:
        newMarks = []
        for c in marks:
            a, o, b = check2[c]
            seena = check.get(a, None)
            seenb = check.get(b, None)
            if seena is not None and seenb is not None:
                if o == 'OR':
                    check[c] = check[a] or check[b]
                elif o == 'AND':
                    check[c] = check[a] and check[b]
                else:
                    check[c] = check[a] ^ check[b]
            else:
                newMarks.append(c)
        marks = newMarks[::]
    
    ans = ''

    for c in z:
        ans += str(check[c])
    
    return int(ans, 2)

print(part1(marks)) # 48508229772400