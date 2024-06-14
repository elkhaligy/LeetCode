from collections import Counter
def commonChars(words: list[str]) -> list[str]:
    lst = []
    ans = []
    for word in words:
        lst.append(Counter(word))
    print(lst)
    flag = False
    # ["cool","lock","cook"]
    for c in words[0]:
        if c in ans:
            continue
        for counter in lst:
            if c not in counter:
                flag = True
                break
        if flag == False:
            val = float('inf')
            for counter in lst:
                val = min(val, counter[c])
            while val:
                ans.append(c)
                val -= 1
        flag = False
    return ans

def commonChars_moreopt(words: list[str]) -> list[str]:
    counters_lst = []
    ans_lst = []
    for word in words:
        counters_lst.append(Counter(word))

    flag = False
    min_val = float('inf')

    for key, value in counters_lst[0].items():
        min_val = value

        for counter in counters_lst[1:]:
            if key not in counter:
                flag = True
                break
            else:
                min_val = min(min_val, counter[key])

        if flag == False:
            for _ in range(min_val):
                ans_lst.append(key)
            # ans = [key] * min_val
            # ans_lst.extend(ans)
        flag = False
    return ans_lst


def commonChars_opt1(words: list[str]) -> list[str]:
    common_char = [0] * 26
    current_char = [0] * 26
    result = []
    for c in words[0]:
        common_char[ord(c) - ord('a')] += 1

    for word in words[1:]:
        current_char = [0] * 26

        for c in word:
            current_char[ord(c) - ord('a')] += 1
      
        for i in range(26):
            common_char[i] = min(common_char[i], current_char[i])

    for i in range(26):
        if common_char[i] != 0:
            result += [chr(i + ord('a'))] * common_char[i] 
    
    return result

def commonChars_opt2(words: list[str]) -> list[str]:
    common_counter = Counter(words[0])
    
    for word in words[1:]:
        current_counter = Counter(word)

        for key, value in common_counter.items():
            common_counter[key] = min(common_counter[key], current_counter[key])
        
    result = []
    for key, value in common_counter.items():
        if value == 0:
            continue
        for _ in range(value):
            result.append(key)

    return result
print(commonChars_opt2(words = ["cool","lock","cook"]    ))