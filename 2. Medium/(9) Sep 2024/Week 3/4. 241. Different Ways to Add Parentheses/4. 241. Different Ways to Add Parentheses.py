def diffWaysToCompute(expression: str) -> list[int]:
    operators_dict = \
    {
        '+': lambda op1, op2: op1 + op2,
        '-': lambda op1, op2: op1 - op2,
        '*': lambda op1, op2: op1 * op2,
        '/': lambda op1, op2: int(op1 / op2)
    }
    memo_dict = {}

    def recursive_help(cur_expression):
        results = []

        if cur_expression in memo_dict:
            return [memo_dict[cur_expression]]
        if len(cur_expression) == 0:
            return []
        if len(cur_expression) == 1:
            return [int(cur_expression)]
        if len(cur_expression) == 2 and cur_expression[0].isdigit():
            return [int(cur_expression)]
        
        for index, char in enumerate(cur_expression):
            if char in operators_dict:
                res1 = recursive_help(cur_expression[:index])
                res2 = recursive_help(cur_expression[index + 1:])
                for val1 in res1:
                    for val2 in res2:
                        results.append(operators_dict[char](val1, val2))
        memo_dict[cur_expression] = results[-1]
        return results

    return recursive_help(expression)

print(diffWaysToCompute(expression = "2*3-4*5"))
