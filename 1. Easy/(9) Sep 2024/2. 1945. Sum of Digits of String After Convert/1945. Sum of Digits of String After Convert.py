def getLucky(s: str, k: int) -> int:

    int_rep: str = string_to_int_string(s)
    result: int = digit_sum_k(int_rep, k)

    return result 
def string_to_int_string(s: str) -> str:
    answer = ""

    for c in s:
        answer += str(ord(c) - ord('a') + 1) 
    
    return answer

def digit_sum_k(string, k):

    while k:
        k -= 1
        answer = 0

        for c in string:
            answer += int(c)
        string = str(answer)
    
    return answer
print(getLucky(s = "leetcode", k = 2))
