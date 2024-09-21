def lexicalOrder_nlogn(n: int) -> list[int]:
    lst = [str(num + 1) for num in range(n)]
    return list(map(int, sorted(lst)))


print(lexicalOrder_nlogn(13))