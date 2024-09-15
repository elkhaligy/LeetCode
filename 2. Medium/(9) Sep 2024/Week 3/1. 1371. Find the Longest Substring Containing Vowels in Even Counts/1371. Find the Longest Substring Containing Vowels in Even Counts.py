def findTheLongestSubstring(s: str) -> int:
    # Five bits are sufficient to represent the occurance of vowels
    equivalent_number = {
        'a' : 16,
        'e' : 8,
        'i' : 4,
        'o' : 2,
        'u' : 1
    }

    number_representation = []
    for chr in s:
        if chr in equivalent_number:
            number_representation.append(equivalent_number[chr])
        else:
            number_representation.append(0)
    
    # Compute the prefix xor
    prefix_xor = [0]
    for num in number_representation:
        prefix_xor.append(prefix_xor[-1] ^ num)

    # Compute the maximum length between similar numbers
    indices = {}
    for index, num in enumerate(prefix_xor):
        if num in indices:
            indices[num].append(index)
        else:
            indices[num] = []
            indices[num].append(index)
        
    #print(number_representation, prefix_xor, indices)

    max_difference = 0
    for value_lst in indices.values():
        max_difference = max(max_difference, value_lst[-1] - value_lst[0])
    
    #print(max_difference)
    return max_difference

print(findTheLongestSubstring(s = "eleetminicoworoep"))