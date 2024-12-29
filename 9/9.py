testcase = open('9/9.txt', 'r')

arr = []

counter = 0
for index, ele in enumerate(testcase.read(), 0):
    ele = int(ele)
    if index % 2 == 0:
        while ele:
            arr.append(counter)
            ele -= 1
        counter += 1
    else:
        while ele:
            arr.append('.')
            ele -= 1

testcase.close()

def part1():
    i = 0
    j = len(arr) - 1
    while i < j:
        while arr[i] != '.':
            i += 1
        while arr[j] == '.':
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

part1()

checksum = 0
for i in range(len(arr)):
    if arr[i] == '.':
        break
    checksum += arr[i] * i

print(checksum) # 6344673854800


testcase = open('9/9.txt', 'r').read()

file_id = 0
start = 0

files = {}
blanks = []

for index in range(len(testcase)):
    length = int(testcase[index])
    if index % 2 == 0:
        files[file_id] = [start, length]
        file_id += 1
    else:
        if length > 0:
            blanks.append([start, length])
    start += length

def part2(id):
    while id > 0:
        id -= 1
        for blank in blanks:
            if files[id][0] < blank[0]:
                break
            elif files[id][1] <= blank[1]:
                files[id][0] = blank[0]
                blank[0] = blank[0] + files[id][1]
                blank[1] = blank[1] - files[id][1]
                break

part2(file_id)

checksum2 = 0


for id, (file_start, file_length) in files.items():
    for i in range(file_length):
        checksum2 += id * (file_start + i)

print(checksum2) # 6360363199987
