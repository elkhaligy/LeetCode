class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # Brute force solution
        exp = expression
        while len(exp) > 1:
            # Obtain the max index of a !, & or |
            start = max(exp.rfind("!"), exp.rfind("&"), exp.rfind("|"))
            # Find the first closing parenthesis after the starting index
            end = exp.find(")", start)
            curr_exp = exp[start:end + 1]

            # Operate on the current expression and evaluate it
            operation = curr_exp[0]
            inner_values = curr_exp[2:-1]

            if operation == "!":
                result = "f" if inner_values == "t" else "t"
            elif operation == "&":
                result = "f" if "f" in inner_values else "t"
            elif operation == "|":
                result = "t" if "t" in inner_values else "f"
            
            exp = exp[:start] + result + exp[end + 1:]
        
        return exp == "t"