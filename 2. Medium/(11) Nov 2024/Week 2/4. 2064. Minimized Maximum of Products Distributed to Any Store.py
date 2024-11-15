def minimizedMaximum_bruteForce(n: int, quantities: list[int]) -> int:
    retail_stores = n
    max_quantity = max(quantities)

    for i in range(1, max_quantity + 1):
        required_stores = 0
        for num in quantities:
            required_stores += num // i
            if num % i != 0:
                required_stores += 1
        if required_stores <= retail_stores:
            return i

def minimizedMaximum_binarySearch(n: int, quantities: list[int]) -> int:
    currentStores = n
    left = 1
    right = max(quantities)
    minChunk = float('inf')

    while left <= right:
        mid = left + (right - left) // 2
        if canChunk(quantities, mid, currentStores):
            right = mid - 1
            minChunk = min(minChunk, mid)
        else:
            left = mid + 1

    return minChunk

def canChunk(quantities: int, chunk: int, currentStores: int):
    required_stores = 0
    for num in quantities:
        required_stores += num // chunk
        if num % chunk != 0:
            required_stores += 1
    if required_stores <= currentStores:
        return True
    return False

print(minimizedMaximum_binarySearch(n = 6, quantities = [11,6]))
