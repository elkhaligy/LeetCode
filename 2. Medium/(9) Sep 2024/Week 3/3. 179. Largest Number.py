from functools import cmp_to_key
def largestNumber(nums: list[int]) -> str:
    # I want to custom sort the list, based on the condiction where a + b > b + a
    nums = [str(num) for num in nums]
    lst = sorted(nums, key=cmp_to_key(custom_comparison))
    print(lst)
    if lst[0] == '0':
        return '0'
    return "".join(lst)

def custom_comparison(str1, str2):
    # my conidtions are -1 1 0
    if str1 + str2 > str2 + str1:
        return -1
    elif str2 + str1 > str1 + str2:
        return 1
    else:
        return 0

print(largestNumber(nums = [3,30,34,5,9])) # 9 5 34 3 30