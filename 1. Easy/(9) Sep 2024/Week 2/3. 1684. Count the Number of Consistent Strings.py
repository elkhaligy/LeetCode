class Solution:
    @staticmethod
    def countConsistentStrings_bruteforce(allowed: str, words: list[str]) -> int:
        answer = 0
        allowed_set = set(allowed)

        for word in words:
            cons_flag = True
            for c in word:
                if c not in allowed_set:
                    cons_flag = False
                    break

            if cons_flag:
                answer += 1

        return answer

print(Solution.countConsistentStrings_bruteforce(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))