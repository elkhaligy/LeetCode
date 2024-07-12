def distributeCandies_hash_table(candyType: list[int]) -> int:
    candies_num = len(candyType) // 2
    freq_dict = {}

    for type in candyType:
        freq_dict[type] = freq_dict.get(type, 0) + 1
    
    different_candies = len(freq_dict.keys())
    return different_candies if candies_num >= different_candies else candies_num

def distributeCandies_set(candyType: list[int]) -> int:
    candies_num = len(candyType) // 2
    different_candies = len(set(candyType))

    return different_candies if candies_num >= different_candies else candies_num

def distributeCandies_set_sol2(candyType: list[int]) -> int:
    return min(len(candyType) // 2, len(set(candyType)))
print(distributeCandies_set_sol2(candyType = [1,1,2,2,3,3]))