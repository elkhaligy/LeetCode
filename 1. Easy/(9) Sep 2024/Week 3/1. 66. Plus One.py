def plusOne_oneliner(digits: list[int]) -> list[int]:
    return list(map(int, (list(str(int("".join(list(map(str, digits)))) + 1)))))

def plusOne(digits: list[int]) -> list[int]:
    digits = digits[::-1]
    digits[0] += 1

    result = []
    tens = 0
    for i in range(len(digits)):
        digits[i] += tens
        tens -= 1
        if tens < 0:
            tens = 0

        if digits[i] == 10:
            digits[i] = 0
            tens += 1
    
    if tens:
        digits.append(1)

    print(digits)
    return digits[::-1]

print(plusOne(digits = [9,9,9]))