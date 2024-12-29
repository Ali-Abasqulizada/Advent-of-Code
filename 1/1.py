testcase = open('1/1.txt', 'r')
left_arr = []
right_arr = []
for line in testcase:
    left, right = line.split()
    left_arr.append(int(left))
    right_arr.append(int(right))
left_arr.sort()
right_arr.sort()
ans = 0
for i in range(len(left_arr)):
    ans += abs(left_arr[i] - right_arr[i])
print(ans) # 1666427

check = {}
ans2 = 0
leftIndex = 0
rightIndex = 0
while rightIndex < len(right_arr) and leftIndex < len(left_arr):
    if left_arr[leftIndex] == right_arr[rightIndex]:
        check[left_arr[leftIndex]] = check.get(left_arr[leftIndex], 0) + 1
        rightIndex += 1
    elif left_arr[leftIndex] < right_arr[rightIndex]:
        leftIndex += 1
    else:
        rightIndex += 1
for i, j in check.items():
    ans2 += (i * j)

print(ans2) # 24316233