def generateParenthesis(n: int) -> list[str]:
    ans = []
    def backtracking(result, open_cnt, close_cnt):
        if open_cnt == close_cnt == n:
            ans.append(result)
            return

        if open_cnt < n:
            backtracking(result + '(', open_cnt + 1, close_cnt)
        if close_cnt < open_cnt:
            backtracking(result + ')', open_cnt, close_cnt + 1)
        
    backtracking("", 0, 0)
    return ans



print(generateParenthesis(3))