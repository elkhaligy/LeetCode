def uncommonFromSentences(s1: str, s2: str) -> list[str]:
    s1_list = s1.split()
    s2_list = s2.split()
    s1_dict = {}
    s2_dict = {}
    for word in s1_list:
        s1_dict[word] = s1_dict.get(word, 0) + 1
    for word in s2_list:
        s2_dict[word] = s2_dict.get(word, 0) + 1

    result = []
    for word in s1_dict.keys():
        if word not in s2_dict.keys() and s1_dict[word] == 1:
            result.append(word)

    for word in s2_dict.keys():
        if word not in s1_dict.keys() and s2_dict[word] == 1:
            result.append(word)        
        
    return result

def uncommonFromSentences_sol2(s1: str, s2: str) -> list[str]:
    freq_dict = {}
    for word in s1.split():
        freq_dict[word] = freq_dict.get(word, 0) + 1
    for word in s2.split():
        freq_dict[word] = freq_dict.get(word, 0) + 1

    result = []
    for word in freq_dict.keys():
        if freq_dict[word] == 1:
            result.append(word)

    return result   
print(uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))