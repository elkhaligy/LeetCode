from collections import defaultdict
from collections import Counter
def remove_duplicates(input_string):
    seen = set()
    result = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
def isIsomorphic(s: str, t: str) -> bool:
    s_unq = remove_duplicates(s)
    t_unq = remove_duplicates(t)
    map_dct = defaultdict(chr)

    for c in s_unq:
        map_dct[c] = c
    for c1, c2 in zip(s_unq, t_unq):
            map_dct[c1] = c2
    
    values_occu = Counter(map_dct.values())

    for key, value in map_dct.items():
         if values_occu[value] > 1 and key != value:
            map_dct[key] = key
            values_occu[value] -= 1
    s_lst = list(s)
    for i in range(len(s_lst)):
        s_lst[i] = map_dct[s_lst[i]]

    return ''.join(s_lst) == t
def isIsomorphicSol2_notworking(s: str, t: str) -> bool:
    zipped = zip(s, t)
    occu_dct = defaultdict(chr)


    for i in set(zipped):

        occu_dct[i[0]] = i[1] 

    for i in s:
        if i not in occu_dct:
            occu_dct[i] = i
    
    ans = ""
    
    for c in s:
        ans += occu_dct[c]
    
    return ans == t


print(isIsomorphicSol2(s = "badc", t = "baba"))