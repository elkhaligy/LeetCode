def canBeEqual(target: list[int], arr: list[int]) -> bool:
    return sorted(target) == sorted(arr)