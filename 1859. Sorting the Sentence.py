from collections import Counter
def sortSentence(s: str) -> str:
    my_dict = {}
    words_lst = s.split()
    for item in words_lst:
        my_dict[item[-1]] = item[:-1]
    
    #print(my_dict)
    ans = [''] * len(words_lst)

    for key, value in my_dict.items():
        ans[int(key) - 1] = value
    
    #print(ans)
    return ' '.join(ans)
    


print(sortSentence(s = "is2 sentence4 This1 a3"))
