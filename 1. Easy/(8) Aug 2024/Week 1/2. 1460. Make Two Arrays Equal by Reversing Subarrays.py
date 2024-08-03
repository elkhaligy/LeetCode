from collections import Counter
def canBeEqual_nlogn(target: list[int], arr: list[int]) -> bool:
    return sorted(target) == sorted(arr)

def canBeEqual_n(target: list[int], arr: list[int]) -> bool:
    freq_1 = Counter(target)
    freq_2 = Counter(arr)
    return freq_1 == freq_2