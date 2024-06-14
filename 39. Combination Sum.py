def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    cur_path = []
    def backtracking():
        su = sum(cur_path)
        if su == target:
            if sorted(cur_path) in result:
                return
            else:
                result.append(sorted(cur_path))
            return
        elif su > target:
            return
        for num in candidates:
            cur_path.append(num)
            backtracking()
            cur_path.pop()

    backtracking()
    return result


combinationSum(candidates = [2,3,5], target = 8)