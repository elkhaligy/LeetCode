def minimumSteps(s: str) -> int:
    # For each one I need to know how many zeros on its right
    n = len(s)
    right_zeros = [0] * n

    zero_count = 0
    for i in range(n - 1, -1, -1):
        if s[i] == '0':
            zero_count += 1
        else:
            right_zeros[i] = zero_count

    print(right_zeros)

    return sum(right_zeros)


print(minimumSteps(s = "1100"))