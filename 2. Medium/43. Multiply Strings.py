def multiply(num1: str, num2: str) -> str:
    num1 = num1[::-1]
    num2 = num2[::-1]
    ans_arr = [0] * (len(num1) + len(num2) + 1)

    # Get ans_arr
    for i1, n1 in enumerate(num1):
        for i2, n2 in enumerate(num2):
            ans_arr[i1 + i2] += (int(n1)) * (int(n2))
    
    # Fix the carry
    prev_tens = 0
    for i in range(len(ans_arr)):
        if prev_tens > 0:
            ans_arr[i] += prev_tens
            prev_tens = 0
        while ans_arr[i] >= 10:
            ans_arr[i] -= 10
            prev_tens += 1

    
    # Ignore left zeros
    start = 0
    ans_arr = ans_arr[::-1]
    print(ans_arr)
    for i in range(len(ans_arr)):
        if ans_arr[i] == 0:
            start = i
            continue
        else:
            start = i
            break
    # if start == len(ans_arr) - 1:
    #     return "0"
    print(start)
    return ''.join(map(str, ans_arr[start:]))


print(multiply(num1 = "2", num2 = "3"))