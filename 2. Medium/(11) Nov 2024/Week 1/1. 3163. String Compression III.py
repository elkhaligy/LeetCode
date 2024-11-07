def compressedString(word: str) -> str:
    if len(word) == 1:
        return "1" + word[0]

    ans = ""
    prev_chr = word[0]
    count = 1
    for chr in word[1:]:
        if chr != prev_chr:
            if count != 0:
                ans += str(count)
                ans += prev_chr
            prev_chr = chr
            count = 1
        else:
            count += 1
            if count == 9:
                ans += str(count)
                ans += prev_chr
                count = 0
    if count != 0:
        ans += str(count)
        ans += prev_chr
    return ans

def compressedString_sol2(word: str) -> str:
    if len(word) == 1:
        return "1" + word[0]

    ans = ""
    prev_chr = word[0]
    current_window = {word[0] : 1}

    for chr in word[1:]:
        if chr != prev_chr:
            repitions = current_window[prev_chr]
            while repitions > 9:
                ans += "9" + prev_chr
                repitions -= 9
            if repitions != 0:
                ans += str(repitions) + prev_chr
                repitions = 0
            current_window[chr] = 1
            prev_chr = chr
        else:
            current_window[chr] += 1

    repitions = current_window[prev_chr]
    while repitions > 9:
        ans += "9" + prev_chr
        repitions -= 9
    if repitions != 0:
        ans += str(repitions) + prev_chr
        repitions = 0

    return ans

def compressedString_sol3(word: str) -> str:
    curr_idx = 0
    ans = ""

    while curr_idx < len(word):
        count = 0
        curr_chr = word[curr_idx]

        while curr_idx < len(word) and word[curr_idx] == curr_chr and count < 9:
            count += 1
            curr_idx += 1

        ans += str(count) + curr_chr
    
    return ans

print(compressedString_sol3(word = "aaaaaaaaay"))
