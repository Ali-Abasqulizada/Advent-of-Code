testcase = open('7/7.txt', 'r')

def find(ans, check, i):
    if i == len(nums):
        return ans == check
    elif check > ans:
        return False
    return find(ans, check * int(nums[i]), i + 1) or find(ans, check + int(nums[i]), i + 1)

def find2(ans, check,  i):
    if i == len(nums):
        return ans == check
    if check > ans:
        return False
    return find2(ans, check + int(nums[i]), i + 1) or \
        find2(ans, check * int(nums[i]), i + 1) or \
        find2(ans, int(str(check) + nums[i]), i + 1)

result = 0
result2 = 0

for line in testcase:
    ans, nums = line.split(': ')
    nums = nums.split()
    if find(int(ans), int(nums[0]), 1):
        result += int(ans)
    elif find2(int(ans), int(nums[0]), 1):
        result2 += int(ans)

testcase.close()

print(result) # 3598800864292
print(result + result2) # 340362529351427