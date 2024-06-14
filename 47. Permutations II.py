def permuteUnique(nums: list[int]) -> list[list[int]]:
    result_lst = []
    
    def backtracking(current_lst: list[int], taken_indices) -> None:
        if len(current_lst) == len(nums):
            if current_lst in result_lst:
                return
            result_lst.append(current_lst[:])
            return

        for idx, num in enumerate(nums):
            if idx in taken_indices:
                continue
            current_lst.append(num)
            taken_indices.add(idx)
            backtracking(current_lst, taken_indices)
            taken_indices.remove(idx)
            current_lst.pop() 

    backtracking([], set())
    return result_lst


print(permuteUnique([1,2,3]))