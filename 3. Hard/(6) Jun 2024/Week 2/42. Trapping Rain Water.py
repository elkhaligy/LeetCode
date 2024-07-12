def trap(height: list[int]) -> int:
    n = len(height)
    highest_left = [0] * n
    highest_right = [0] * n

    highest_left[0] = 0
    highest_now = 0
    for i in range(1, n):
        highest_now = max(highest_now, height[i - 1])
        highest_left[i] = highest_now
    
    highest_now = 0
    highest_right[-1] = 0
    for i in range(n - 2, -1, -1):
        highest_now = max(highest_now, height[i + 1])
        highest_right[i] = highest_now
    
    print(highest_left, highest_right)
        
    ans = 0
    for i in range(n):
        cur = min(highest_left[i], highest_right[i]) - height[i]
        if cur > 0:
            ans += cur
    return ans


print(trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))