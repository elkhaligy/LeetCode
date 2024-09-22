def lexicalOrder_nlogn(n: int) -> list[int]:
    lst = [str(num + 1) for num in range(n)]
    return list(map(int, sorted(lst)))

def lexicalOrder_n(n: int) -> list[int]:
    result = []
    def generate_lexical(current_number, limit) -> None:
        if current_number > limit:
            return
        result.append(current_number)
        for i in range(10):
            next_num = current_number * 10 + i
            if next_num <= limit:
                generate_lexical(next_num, limit)
            else:
                break

    for i in range(1, 10):
        generate_lexical(i, n)
    return result

print(lexicalOrder_n(13))