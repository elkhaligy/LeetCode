def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    # hello world programmed to work
    # hello world to work
    # our checks will be like that
    # This structure is: count of words to check on start, count of words to check on end
    # If any of these checks went OK, return true
    # 0, 4
    # 1, 3
    # 2, 2
    # 3, 1
    # 4, 0
    
    
    n1, n2 = len(sentence1), len(sentence2)
    # Incase equal lengths
    if n1 == n2:
        return sentence1 == sentence2
    
    sentence1 = sentence1.split()
    sentence2 = sentence2.split()
    checks = []
    smaller_sentense = sentence1 if n1 < n2 else sentence2
    bigger_sentense = sentence1 if n1 > n2 else sentence2
    n1, n2 = len(smaller_sentense), len(bigger_sentense)
    number_of_checks = n1 + 1


    for i in range(number_of_checks):
        checks.append([i, n1 - i])

    for check in checks:
        flag = check_strings(check, smaller_sentense, bigger_sentense)
        if flag:
            return True

    #print(checks)
    return False

def check_strings(check, smaller, bigger):
    left_portion = smaller[:check[0]]
    if check[1] != 0:
        right_portion = smaller[-check[1]:]
    else:
        right_portion = []
    # Left checker
    for i in range(len(left_portion)):
        if left_portion[i] != bigger[i]:
            return False
        
    # Right checker
    r_p_index = len(right_portion) - 1
    for i in range(len(bigger) - 1, -1, -1):
        if r_p_index < 0:
            break
        if right_portion[r_p_index] != bigger[i]:
            return False
        r_p_index -= 1
        
    
    return True 

print(areSentencesSimilar(sentence1 = "Eating right now", sentence2 = "Eating"))