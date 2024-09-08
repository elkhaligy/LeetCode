def chalkReplacer_TLE(chalk: list[int], k: int) -> int:
    n = len(chalk)
    cur_index = 0

    while True:
        if chalk[cur_index % n] > k:
            return cur_index % n
        k -= chalk[cur_index % n]

def chalkReplacer_opt(chalk: list[int], k: int) -> int:
    n = len(chalk)
    cur_index = 0
    lst_sum = sum(chalk)
    remainder =  k % lst_sum

    while True:
        if chalk[cur_index % n] > remainder:
            return cur_index % n
        remainder -= chalk[cur_index % n]
        cur_index += 1

print(chalkReplacer_opt(chalk = [5,1,5], k = 5))
