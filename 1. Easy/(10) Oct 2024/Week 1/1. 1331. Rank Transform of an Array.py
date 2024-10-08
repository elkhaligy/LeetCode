def arrayRankTransform_nlogn(arr: list[int]) -> list[int]:
    if not arr:
        return []
    
    # Dictionary {number : rank}
    ranks_dict = {}
    sorted_arr = sorted(arr)
    curr_rank = 1

    ranks_dict[sorted_arr[0]] = curr_rank
    for num in sorted_arr[1:]:
        if num not in ranks_dict:
            curr_rank += 1
        ranks_dict[num] = curr_rank

    return [ranks_dict[num] for num in arr]




print(arrayRankTransform_n(arr = [1,2,3,4,-1]))