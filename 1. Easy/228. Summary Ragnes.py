def summaryRanges(nums: list[int]) -> list[str]:
    result = []
    first_ind = 0
    last_ind = 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] == 1:
            last_ind = i
            #if i == len(nums) - 1:
                
        else:
            result.append((nums[first_ind], nums[last_ind]))
            first_ind = i
            last_ind = i
    result.append((nums[first_ind], nums[last_ind]))
    #ans = [f"{item[0]}->{item[1]}" for item in result if item[0] != item[1] > 1 else f"{item[0]}"]
    abb = [f"{item[0]}" if item[0] == item[1] else f"{item[0]}->{item[1]}" for item in result]
    print(abb)
    pass


summaryRanges(nums = [0,1,2,4,5,7])