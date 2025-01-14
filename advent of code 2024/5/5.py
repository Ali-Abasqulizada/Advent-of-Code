testcase = open('5/5.txt', 'r')

check = {}
check2 = set()
for line in testcase:
    if '|' not in line:
        break
    l, r = line.split('|')
    check2.add((l, r[:-1]))
    if l in check:
        check[l].append(r[:-1])
    else:
        check[l] = [r[:-1]]

ans = 0

def part2(loserArr):
    repeat = True
    evenOneTime = False
    while repeat:
        repeat = False
        for i in range(len(loserArr)):
            for j in range(i + 1, len(loserArr)):
                for one_check in check2:
                    if (loserArr[j], loserArr[i]) == one_check:
                        loserArr[j], loserArr[i] = loserArr[i], loserArr[j]
                        repeat = True
                        evenOneTime = True
                        continue
    if evenOneTime:
        return False
    return True

ans2 = 0

for line in testcase:
    line = line[:-1]
    arr = line.split(',')
    if part2(arr):
        ans += int(arr[len(arr) // 2])
    else:
        ans2 += int(arr[len(arr) // 2])

print(ans) # 4924
print(ans2) # 6085
