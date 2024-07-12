# To initialize list of lists you have only two options:
# list comprehensions or nested loop
# Explanation under
from collections import defaultdict
from collections import Counter

# O(nlogn)
def topKFrequent(nums: list[int], k: int) -> list[int]:
    occu_dict = defaultdict(int)

    for num in nums:
        occu_dict[num] += 1
    tup_lst = list(occu_dict.items())
    tup_lst.sort(key=lambda x: x[1], reverse=True)
    
    return [tup_lst[i][0] for i in range(k)]

# O(n)
def topKFrequent_Sol2(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    #bucket = [[]] * (n + 1) # bucket: index is frequency THIS IS VERY WRONG, EXPLANATION UNDER
    bucket = [[] for _ in range(n + 1)]
    occu_dict = Counter(nums)
    print(occu_dict)
    for key, value in occu_dict.items():
        bucket[value].append(key)
    
    ans = []
    for i in range(n, -1, -1):
        if len(bucket[i]) > 0:
            for item in bucket[i]:
                if k <= 0:
                    return ans
                ans.append(item)
                k -= 1
    return ans

print(topKFrequent_Sol2(nums = [1,1,1,2,2,3], k = 2))


# Using the expression `bucket = [[]] * (n + 1)` to initialize a list of lists in Python is not recommended, especially if you intend to modify the inner lists individually. This approach creates a list of references to the same inner list, rather than creating separate inner lists.

# Here's an example to illustrate the issue:

# ```python
# n = 3
# bucket = [[]] * (n + 1)
# print(bucket)
# # Output: [[], [], [], []]

# # Modifying one inner list affects all of them
# bucket[0].append(1)
# print(bucket)
# # Output: [[1], [1], [1], [1]]
# ```

# In this case, `bucket[0].append(1)` modifies the same inner list referenced by all elements of `bucket`, leading to unexpected behavior.

# ### Correct Approach

# To create a list of separate inner lists, you should use a list comprehension or another method that ensures each inner list is a distinct object:

# ```python
# # Using list comprehension
# bucket = [[] for _ in range(n + 1)]
# print(bucket)
# # Output: [[], [], [], []]

# # Modifying one inner list does not affect others
# bucket[0].append(1)
# print(bucket)
# # Output: [[1], [], [], []]
# ```

# ### Explanation

# - **`bucket = [[]] * (n + 1)`**: This creates a list containing multiple references to the same inner list. Any modification to one inner list affects all of them because they are all the same object.
# - **`bucket = [[] for _ in range(n + 1)]`**: This creates a list of `n + 1` distinct empty lists. Each inner list is a separate object, so modifications to one do not affect the others.

# Always use the list comprehension approach to avoid unintended side effects when working with a list of lists in Python.








# In Python, initializing a list of lists can be done in several ways depending on your needs. Here are some common methods:

# ### 1. Using List Comprehensions

# List comprehensions provide a concise way to create lists. You can use them to initialize a list of lists as follows:

# ```python
# # Initialize a list of lists with default values (e.g., zeros)
# rows, cols = 3, 4
# list_of_lists = [[0 for _ in range(cols)] for _ in range(rows)]

# print(list_of_lists)
# # Output: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# ```

# ### 2. Using Nested Loops

# You can use nested loops to initialize a list of lists. This method is more verbose but can be useful for complex initializations.

# ```python
# # Initialize a list of lists with specific values
# rows, cols = 3, 4
# list_of_lists = []
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         row.append(0)
#     list_of_lists.append(row)

# print(list_of_lists)
# # Output: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# ```

