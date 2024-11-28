from collections import deque
def dailyTemperatures(temperatures: list[int]) -> list[int]:

    days = 0
    ans = []
    for i in range(len(temperatures)):
        for j in range(i + 1, len(temperatures)):
            days += 1
            if temperatures[i] < temperatures[j]:
                ans.append(days)
                days = 0
                break
            elif j == len(temperatures) - 1:
                days = 0
                ans.append(0)
    ans.append(0)
    return ans

def dailyTemperatures_bruteforce(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    ans = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                ans[i] = j - i
                break
    return ans

def dailyTemperatures_optimized(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    ans = [0] * n
    greatest_stack = []
    greatest_stack.append([temperatures[-1], n - 1])
    for i in range(n - 2, -1, -1):
        while len(greatest_stack) > 0 and temperatures[i] >= greatest_stack[-1][0]:
            greatest_stack.pop()
        if len(greatest_stack) == 0:
            ans[i] = 0
        else:
            ans[i] = greatest_stack[-1][1] - i
        greatest_stack.append([temperatures[i], i])

    return ans

def dailyTemperatures_more_optimized(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    ans = [0] * n
    greatest_stack = deque()
    greatest_stack.appendleft([temperatures[-1], n - 1])
    for i in range(n - 2, -1, -1):
        while greatest_stack and temperatures[i] >= greatest_stack[0][0]:
            greatest_stack.popleft()
        if not greatest_stack:
            ans[i] = 0
        else:
            ans[i] = greatest_stack[0][1] - i
        greatest_stack.appendleft([temperatures[i], i])

    return ans


def dailyTemperatures_nextgreaterelement(temperatures: list[int]) -> list[int]:

    def next_greater_element(nums):
        result = [0] * len(nums)
        stack = []
        
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result
    return next_greater_element(temperatures)

def dailyTemperatures_nextgreaterelement_refactoring(temperatures: list[int]) -> list[int]:

    def find_next_greater_element_index(nums: list[int]) -> list[int]:
        n = len(nums)
        stack = []
        result = [0] * n
        
        for current_index, current_temperature in enumerate(nums):
            while stack and current_temperature > nums[stack[-1]]:
                # Current element is greater than the element in the stack
                previous_index = stack.pop()
                result[previous_index] = current_index - previous_index
            stack.append(current_index)
            
        return result
    
    return find_next_greater_element_index(temperatures)


def dailyTemperatures_practise1(temperatures: list[int]) -> list[int]:
    # Monotonic Decreasing Stack
    monoStack = []
    results = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while monoStack and temperatures[i] > monoStack[-1][0]:
            results[monoStack[-1][1]] = i - monoStack[-1][1]
            monoStack.pop()
            
        monoStack.append((temperatures[i], i))
    
    return results
print(dailyTemperatures_optimized([73,74,75,71,69,72,76,73]))
