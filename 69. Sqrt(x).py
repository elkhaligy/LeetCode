def mySqrt(x: int) -> int:
    prev = 1
    for i in range( 2 ,(x//2 + 1)):
        
        if i * i > x:
            return prev
        else:
            prev = i

    return prev
    
def mySqrt_sol2(x: int) -> int:
    if x < 2:
        return x
    left, right = 2, x//2

    while left <= right:
        mid = (left + right) // 2

        square = mid * mid
        if square == x:
            return mid
        elif square > x:
            right = mid - 1
        elif square < x:
            left = mid + 1
    return right

print(mySqrt_sol2(8))