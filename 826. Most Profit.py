def maxProfitAssignment(difficulty: list[int], profit: list[int], worker: list[int]) -> int:
    combined = list(zip(difficulty, profit))
    combined.sort(key=lambda element: element[1], reverse=True)

    max_profit = 0
    for w in worker:
        for element in combined:
            if w >= element[0]:
                w -= element[0]
                max_profit += element[1]
                break
    return max_profit

def maxProfitAssignment_opt_binarysearch(difficulty: list[int], profit: list[int], worker: list[int]) -> int:
    combined_tup = list(zip(difficulty, profit))
    combined_tup.sort(key=lambda element: element[0])
    combined = []

    for item in combined_tup:
        combined.append(list(item))

    max_profit = 0

    for i in range(1, len(combined)):
        combined[i][1] = max(combined[i - 1][1], combined[i][1])

    for w in worker:
        l, r = 0, len(combined) - 1
        cur_profit = 0
        while l <= r:
            mid = (l + r) // 2
            if combined[mid][0] <= w:
                cur_profit = max(cur_profit, combined[mid][1])
                l = mid + 1
            else:
                r = mid - 1
        max_profit += cur_profit
        
    return max_profit

print(maxProfitAssignment_opt(difficulty =[5,50,92,21,24,70,17,63,30,53], profit = [68,100,3,99,56,43,26,93,55,25], worker = [96,3,55,30,11,58,68,36,26,1]))
