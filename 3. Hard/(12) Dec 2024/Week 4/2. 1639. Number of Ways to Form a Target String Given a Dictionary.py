class Solution:
    def numWays(self, words, target):
        # Our DP state matrix tracks two states, the current word index and the current target index
        # so we need a 2D matrix with len(words[0]) rows and len(target) columns
        # so for example dp[0][1] will be the state of that we're in the word index 0 and target index 1
        dp = [[-1] * len(target) for _ in range(len(words[0]))]

        # Character frequency has words length rows and 26 length columns to count frequency
        # at each row we need the frequency of character at this index
        char_frequency = [[0] * 26 for _ in range(len(words[0]))]

        # Store the frequency of every character at every index.
        # words = ["acca","bbbb","caca"]
        # In the above input index 0 has 'a', 'b', 'c' so it will be [1, 1, 1, 0, 0...]
        # index 1 has 'c', 'b', 'a' so it will also be [1, 1, 1, 0 , 0 ...]
        for i in range(len(words)):
            for j in range(len(words[0])):
                character = ord(words[i][j]) - 97
                char_frequency[j][character] += 1

        def get_words(words_index, target_index):
            # We have two base cases
            # If the target index is equal to the length of the target then we have a possible solution, return 1 to be added to the number of ways
            if target_index == len(target):
                return 1
            # If the word index reached the end then there's no possible solution return 0
            if (words_index == len(words[0])):
                return 0
            
            # Here we're using memoization, if you found the solution return it instantly
            if dp[words_index][target_index] != -1:
                return dp[words_index][target_index]

            count_ways = 0
            cur_pos = ord(target[target_index]) - 97
            # Don't match any character of target with any word.
            count_ways += get_words(words_index + 1, target_index)
            # Multiply the number of choices with getWords and add it to count.
            count_ways += char_frequency[words_index][cur_pos] * get_words(words_index + 1, target_index + 1)
            dp[words_index][target_index] = count_ways % 1000000007
            
            return dp[words_index][target_index]
        

        return get_words(words_index=0, target_index=0)





solObj = Solution()
print(solObj.numWays(words = ["acca","bbbb","caca"], target = "aba"))