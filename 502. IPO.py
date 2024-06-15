import heapq
def findMaximizedCapital_32o35(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    picked_projects = 0
    sorted_projects = list(zip(profits, capital))
    sorted_projects = [item for item in sorted_projects if item[0] != 0]
    sorted_projects.sort(key=lambda a: a[0])
    picked = [0] * len(sorted_projects)
    picked_flag = False
    
    while picked_projects < k:

        for ind in range(len(sorted_projects) - 1, -1, -1):
            if picked[ind] != 1 and w >= sorted_projects[ind][1]:
                w += sorted_projects[ind][0]
                picked[ind] = 1
                picked_projects += 1
                picked_flag = True
                break

        if not picked_flag:
            return w
        picked_flag = False
                
    return w
    
def findMaximizedCapital_opt(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    min_heap = []
    max_heap = []
    
    for ind in range(len(profits)):
        heapq.heappush(min_heap, (capital[ind], profits[ind]))
        
    while k:
        while min_heap and min_heap[0][0] <= w:
            _, project_protif = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -project_protif)
            
        if not max_heap:
            break
        
        w += -heapq.heappop(max_heap)
        k -= 1
    return w

print(findMaximizedCapital_opt(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]))
