def isSubstringPrefix(sentence: str, searchWord: str):
    words = sentence.split()
    for index, word in enumerate(words):
        if word.find(searchWord) != 0:
            return index + 1
    
    return -1