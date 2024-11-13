def minimumMountainRemovals(nums: list[int]) -> int:
    n = len(nums)

    increasing_subseq = [1] * n
    decreasing_subseq = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                increasing_subseq[i] = max(increasing_subseq[i], increasing_subseq[j] + 1)
    #print(increasing_subseq)

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                decreasing_subseq[i] = max(decreasing_subseq[i], decreasing_subseq[j] + 1)
    #print(decreasing_subseq)
    min_removals = float("inf")
    for i in range(n):
        if increasing_subseq[i] > 1 and decreasing_subseq[i] > 1:
            min_removals = min(min_removals, n - increasing_subseq[i] - decreasing_subseq[i] + 1)

    return min_removals

minimumMountainRemovals(nums = [2,1,1,5,6,2,3,1])