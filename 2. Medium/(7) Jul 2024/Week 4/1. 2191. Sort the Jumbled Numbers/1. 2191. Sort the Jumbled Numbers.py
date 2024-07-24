def sortJumbled(mapping: list[int], nums: list[int]) -> list[int]:
    mapped_nums = []
    for num in nums:
        mapped_nums.append(get_mapping(num, mapping))

    zipped_nums = zip(nums, mapped_nums)
    zipped_nums = sorted(zipped_nums, key= lambda a: a[1])

    answer = []
    for tup in zipped_nums:
        answer.append(tup[0])
    
    return answer

def get_mapping(num: int, mapping: list[int]) -> int:
    num_str = str(num)
    ans_str = ""
    for digit in num_str:
        ans_str += str(mapping[int(digit)])
    
    return int(ans_str)
print(sortJumbled(mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]))
