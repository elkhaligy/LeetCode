def combinationSum_timelimit(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    cur_path = []
    cur_index = []
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
        for i, num in enumerate(candidates):
            if i in cur_index:
                continue
            cur_index.append(i)
            cur_path.append(num)
            backtracking()
            cur_index.pop()
            cur_path.pop()

    backtracking()
    return result


print(combinationSum_timelimit(candidates = [10,1,2,7,6,1,5], target = 8))