testcase = open('2/2.txt', 'r').read().split('\n')
safe = 0
for line in testcase:
    arr = line.split()
    increase = True
    if int(arr[0]) == int(arr[1]):
        continue
    elif int(arr[0]) > int(arr[1]):
        increase = False
    if increase:
        correct = True
        for i in range(1, len(arr)):
            diff = int(arr[i]) - int(arr[i - 1])
            if diff <= 0 or diff > 3:
                correct = False
                break
        if correct:
            safe += 1
    else:
        correct = True
        for i in range(len(arr) - 1):
            diff = int(arr[i]) - int(arr[i + 1])
            if diff <= 0 or diff > 3:
                correct = False
                break
        if correct:
            safe += 1
print(safe) # 516

def check(arr):
    increase = True
    if int(arr[0]) == int(arr[1]):
        return False
    elif int(arr[0]) > int(arr[1]):
        increase = False
    if increase:
        for i in range(1, len(arr)):
            diff = int(arr[i]) - int(arr[i - 1])
            if diff <= 0 or diff > 3:
                return False
        return True
    else:
        for i in range(len(arr) - 1):
            diff = int(arr[i]) - int(arr[i + 1])
            if diff <= 0 or diff > 3:
                return False
        return True
    

safe2 = 0
for line in testcase:
    arr = line.split()
    if check(arr=arr):
        safe2 += 1
        continue

    for i in range(len(arr)):
        newArr = []
        for j in range(len(arr)):
            if i != j:
                newArr.append(arr[j])
        if check(arr=newArr):
            safe2 += 1
            break
print(safe2) # 561