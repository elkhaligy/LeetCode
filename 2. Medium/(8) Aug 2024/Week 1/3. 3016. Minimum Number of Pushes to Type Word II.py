from collections import Counter

def minimumPushes(word: str) -> int:
    # Sort the letters depending on their frequency
    letters_freq = Counter(word)
    unique_letters = sorted(letters_freq, key = letters_freq.get, reverse = True)

    # Apply the algorithm, overall nlogn
    cost_dict = {}
    counter = 0
    additional_cost = 0
    for i, c in enumerate(unique_letters):
        if counter % 8 == 0 and i > 0:
            additional_cost += 1
        cost_dict[c] = 1 + additional_cost
        counter += 1

    ans = 0   
    for c in word:
        ans += cost_dict[c]
    
    return ans



print(minimumPushes(word = "aabbccddeeffgghhiiiiii"))