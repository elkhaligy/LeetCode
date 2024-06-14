from collections import Counter
def countAndSay(n: int) -> str:
    my_str = "1"
    for _ in range(n - 1):
        arr = freq_func(my_str)
        new_str = ""
        for item in arr:
            new_str += item[1]
            new_str += item[0]
        my_str = new_str

    return my_str

def freq_func(s: str) -> list[list[str]]:
    cur_str = ""
    result = []
    cur_str += s[0]
    for c in s[1:]:
        if c in cur_str:
            cur_str += c
        else:
            result.append([cur_str[0], str(len(cur_str))])
            cur_str = ""
            cur_str += c
    result.append([cur_str[0], str(len(cur_str))])
    return result

def freq_func_2(s: str) -> list[list[str]]:
    cur_str = ""
    result = []
    cur_str = ""
    prev = 0
    cur = 1
    while cur < len(s):
        if s[cur] == s[prev]:
            cur_str += s[prev]
        else:
            cur_str += s[prev]
            result.append([cur_str[0], str(len(cur_str))])
            cur_str = ""
        cur += 1
        prev += 1
    cur_str += s[prev]
    print(cur_str)
    print(result)
    result.append([cur_str[0], str(len(cur_str))])

    return result
print(freq_func_2("11211212"))