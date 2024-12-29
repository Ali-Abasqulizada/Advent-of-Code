import re

testcase = open('3/3.txt', 'r').read()
pattern = r'mul\((\d+),(\d+)\)'
product = 0
for line in testcase.split('\n'):
    one_line = re.findall(pattern, line)
    for l, r in one_line:
        product += int(l) * int(r)

print(product) # 191183308

arr = re.split(r"don't\(\).*?do\(\)", testcase, flags=re.DOTALL)
pattern = r'mul\((\d+),(\d+)\)'
product = 0
for line in arr:
    matches = re.findall(pattern, line)
    for l, r in matches:
        product += int(l) * int(r)

print(product) # 92082041