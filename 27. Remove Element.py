def removeElement(nums: list[int], val: int) -> int:
    i = 0
    end = len(nums)
    while i < end:
        if nums[i] == val:
            nums.pop(i)
            end -= 1
            if i > 0:
                i -= 1
        else:
            i += 1

    return len(nums)


nums = [1]
removeElement(nums, 2)
print(nums)