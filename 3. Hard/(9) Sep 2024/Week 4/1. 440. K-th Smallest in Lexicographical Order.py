def findKthNumber_TLE(n: int, k: int) -> int:
    # This solution is o(n), but gives TLE too!!
    count = 0

    def generate_lexical(current_number, limit) -> None:
        nonlocal count
        if current_number > limit:
            return
        count += 1
        if count == k:
            return current_number
        for i in range(10):
            next_num = current_number * 10 + i
            if next_num <= limit:
                loc = generate_lexical(next_num, limit)
                if loc != None:
                    return ans
            else:
                break

    for i in range(1, 10):
        ans = generate_lexical(i, n) 
        if ans != None:
            return ans

def findKthNumber_Editorial(n, k):
    # To count how many numbers exist between prefix1 and prefix2
    def count_steps(n, prefix1, prefix2):
        steps = 0
        while prefix1 <= n:
            steps += min(n + 1, prefix2) - prefix1
            prefix1 *= 10
            prefix2 *= 10
        return steps
    
    curr = 1
    k -= 1
    while k > 0:
        step = count_steps(n, curr, curr + 1)
        # If the steps are less than or equal to k, we skip this prefix's subtree
        if step <= k:
            # Move to the next prefix and decrease k by the number of steps we skip
            curr += 1
            k -= step
        else:
            # Move to the next level of the tree and decrement k by 1
            curr *= 10
            k -= 1

    return curr



print(findKthNumber_Editorial(10, 9))
