class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += str(len(string)) + "@" + string
        
        return encoded_str
           
    def decode(self, s: str) -> list[str]:
        str_index = 0
        end_index = 0
        ans = []

        while str_index < len(s):
            cur_str = ""
            while s[end_index] != "@":
                end_index += 1

            cur_word_len = int(s[str_index:end_index])
            for i in range(end_index + 1, cur_word_len + end_index + 1):
                cur_str += s[i]
            ans.append(cur_str)
            str_index = end_index + cur_word_len + 1
            end_index = str_index

        print(ans)
        return ans


# @2we3@say1@:3@yes10@!@#$%^&*()

input_str = ["we","say",":","yes","!@#$%^&*()"]
sol_obj = Solution()
encoded_str = sol_obj.encode(input_str)
sol_obj.decode(encoded_str)