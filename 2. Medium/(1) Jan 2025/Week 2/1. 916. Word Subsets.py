from collections import Counter, defaultdict
def wordSubsets(words1: list[str], words2: list[str]) -> list[str]:
    # Combine all words in words2
    # Create a hashmap that maps each character in the combined words2 to their occurence
    # For each word in words 1 create a counter for it too
    # Compare the counter of the currnet words with the counter of the combined words2
    # A word passes if it has the character in cobmined words2 and the same or bigger frequency
    combinedCounter = defaultdict(int)
    for word in words2:
        currCounter = Counter(word)
        for letter in currCounter:
            combinedCounter[letter] = max(combinedCounter[letter], currCounter[letter])
    ans = []
    for word in words1:
        flag = True
        currCounter = Counter(word)
        # print(currCounter)
        for key, val in combinedCounter.items():
            if key in currCounter and currCounter[key] >= val:
                continue
            else:
                flag = False
                break
        if flag:
            ans.append(word)

    return ans


print(wordSubsets(["cccbb"],["add","b","ba","ada","dcd"]))
