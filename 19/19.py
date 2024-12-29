from functools import cache

testcase = open('19/19.txt', 'r').read().split('\n\n')

stripes = testcase[0].split(', ')
towels = testcase[1].split('\n')

@cache
def part1(start: int, towel: str):
    if start == len(towel):
        return 1
    elif start > len(towel):
        return 0
    ans2 = 0
    for stripe in stripes:
        if towel[start:].startswith(stripe):
            ans2 += part1(start + len(stripe), towel)
    return ans2

ans = 0
ans2 = 0

for towel in towels:
    result = part1(0, towel)
    ans2 += result
    if result:
        ans += 1

print(ans) # 220
print(ans2) # 565600047715343