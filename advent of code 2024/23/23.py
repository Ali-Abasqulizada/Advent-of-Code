testcase = open('23/23.txt', 'r').read().split('\n')

check = {}

for line in testcase:
    a, b = line.split('-')
    if a in check:
        check[a].append(b)
    else:
        check[a] = [b]
    if b in check:
        check[b].append(a)
    else:
        check[b] = [a]
    
def part1():
    ans = set()
    for one in check:
        for two in check[one]:
            for three in check[two]:
                if three != one:
                    if one in check[three]:
                        ans.add(tuple(sorted([one, two, three])))
    counter = 0
    for sequence in ans:
        for ele in sequence:
            if ele[0] == 't':
                counter += 1
                break
    return counter

def part2():
    ans = []
    for one in check:
        helper = [check[one][0]]
        for two_index in range(1, len(check[one])):
            seen = True
            for helper_index in range(len(helper) - 1, -1, -1):
                if check[one][two_index] not in check[helper[helper_index]]:
                    seen = False
                    break
            if seen:
                helper.append(check[one][two_index])
        if len(ans) < len(helper) + 1:
            ans = helper + [one]
    return ','.join(sorted(ans))


print(part1()) # 1378
print(part2()) # bs,ey,fq,fy,he,ii,lh,ol,tc,uu,wl,xq,xv