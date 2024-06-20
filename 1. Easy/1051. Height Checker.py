def heightChecker_builtinsort(heights: list[int]) -> int:
    ordered = sorted(heights)
    ans = 0

    for i in range(len(heights)):
        if heights[i] != ordered[i]:
            ans += 1
    return ans

def heightChecker_bubblesort(heights: list[int]) -> int:
    
    def bubble_sort(lst: list[int]) -> None:
        # Bubble sort
        n = len(lst)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if lst[j + 1] < lst[j]:
                    lst[j + 1], lst[j] = lst[j], lst[j + 1]

    ans = 0
    sorted_heights = heights[:]
    bubble_sort(sorted_heights)
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            ans += 1
    return ans

def heightChecker_countingsort(heights: list[int]) -> int:
    
    def counting_sort(lst: list[int]) -> None:
        min_value, max_value = min(lst), max(lst)
        counts = {}
        
        for val in lst:
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1
        
        ind = 0
        for val in range(min_value, max_value + 1):
            while counts.get(val, 0) > 0:
                lst[ind] = val
                ind += 1
                counts[val] -= 1

       # print(lst)
    ans = 0
    sorted_heights = heights[:]
    counting_sort(sorted_heights)
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            ans += 1
    return ans

print(heightChecker_countingsort(heights = [1,1,4,2,1,3]))