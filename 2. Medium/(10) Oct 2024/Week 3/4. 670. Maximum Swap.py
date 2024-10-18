def maximumSwap(num: int) -> int:
    num_str = list(str(num))
    n = len(num_str)

    highest_next_index = [0] * n
    highest_next_index[n - 1] = n - 1

    for i in range(n - 2, -1, -1):
        if num_str[i] > num_str[highest_next_index[i + 1]]:
            highest_next_index[i] = i
        else:
            highest_next_index[i] = highest_next_index[i + 1]

    for i in range(n):
        if num_str[i] < num_str[highest_next_index[i]]:
            num_str[i], num_str[highest_next_index[i]] = num_str[highest_next_index[i]], num_str[i]
            break

    return int("".join(num_str))