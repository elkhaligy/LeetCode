def reverseParentheses(s: str) -> str:
    stack = []
    for chr in s:
        if chr == ')':
            curr_chr = stack.pop()
            curr_str = ""

            if curr_chr != '(':
                curr_str = curr_chr

            while curr_chr != '(':
                
                curr_chr = stack.pop()
                if curr_chr != '(':
                    curr_str += curr_chr

            for c in curr_str:
                stack.append(c)

            #print(curr_str)
        else:
            stack.append(chr)

    return "".join(stack)

print(reverseParentheses(s = "(ed(et(oc))el)"))
