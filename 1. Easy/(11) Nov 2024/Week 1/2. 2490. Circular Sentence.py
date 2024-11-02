def isCircularSentence(sentence: str) -> bool:
    lst = sentence.split()
    if lst[0][0] != lst[-1][-1]:
        return False
    prev_word = lst[0]

    for word in lst[1:]:
        if word[0] != prev_word[-1]:
            return False
        prev_word = word

    return True


print(isCircularSentence(sentence = "leetcode exercises sound delightful"))
