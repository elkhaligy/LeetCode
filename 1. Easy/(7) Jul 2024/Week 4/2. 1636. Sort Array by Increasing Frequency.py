def frequencySort(nums: list[int]) -> list[int]:
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    sorted_to_keys = list(sorted(freq_dict.keys(), reverse=True))
    sorted_dict = {key: freq_dict[key] for key in sorted_to_keys}
    #print(freq_dict, sorted_dict)
    sorted_to_freq = sorted(sorted_dict, key= sorted_dict.get)

    answer = []
    for num in sorted_to_freq:
        while sorted_dict[num]:
            answer.append(num)
            sorted_dict[num] -= 1
    
    return answer


print(frequencySort(nums = [2,3,1,3,2]))
