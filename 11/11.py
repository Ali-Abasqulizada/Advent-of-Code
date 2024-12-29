testcase = open('11/11.txt', 'r').read()

myarr = testcase.split()

def part1(arr):
    newArr = []
    for ele in arr:
        if ele == '0':
            newArr.append('1')
        elif len(ele) % 2 == 0:
            newArr.append(ele[:len(ele)//2])
            if ele[len(ele)//2:][0] == '0':
                second = ''
                index = 0
                for i in ele[len(ele)//2:]:
                    if i == '0':
                        index += 1
                    else:
                        break
                second = ele[len(ele)//2:][index:]
                newArr.append(second) if second != '' else newArr.append('0')
            else:
                newArr.append(ele[len(ele)//2:])
        else:
            newArr.append(str(int(ele) * 2024))
    return newArr

from functools import cache

@cache
def part2(myTuple, times):
    myNewTuple = []
    for ele in myTuple:
        length = len(str(ele))
        if ele == 0:
            myNewTuple.append(1)
        elif length % 2 == 0:
            myNewTuple.append(int(str(ele)[:length//2]))
            myNewTuple.append(int(str(ele)[length//2:]))
        else:
            myNewTuple.append(ele * 2024)
    times -= 1
    if times == 0:
        return len(myNewTuple)
    result = 0
    for oneMyTuple in myNewTuple:
        result += part2((oneMyTuple, ), times)
    return result


for _ in range(25):
    myarr = part1(myarr)[::]

print(len(myarr)) # 235850
print(part2(tuple(map(int, testcase.split())), 75)) # 279903140844645