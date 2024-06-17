import math
def evalRPN(tokens: list[str]) -> int:
    stack = []
    def is_integer(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
        
    for chr in tokens:
        if is_integer(chr):
            stack.append(chr)
        else:
            operator = chr
            operand_2 = int(stack.pop())
            operand_1 = int(stack.pop())
            result = eval(f"{operand_1} {operator} {operand_2}")
            if operator == '/':
                if result < 0:
                    result = math.ceil(result)
                else:
                    result = math.floor(result)
            stack.append(str(result))   
    return int(stack[-1])

def evalRPN_optimized(tokens: list[str]) -> int:
    stack = []
        
    for chr in tokens:
        if chr == '+':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 + op2)
        elif chr == '-':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 - op2)
        elif chr == '*':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 * op2)
        elif chr == '/':
            op2 = stack.pop()
            op1 = stack.pop()
            res = op1 / op2
            if res < 0:
                res = math.ceil(res)
            else:
                res = math.floor(res)
            stack.append(res)
        else:
            stack.append(int(chr))
    return stack[-1]


def evalRPN_refactord(tokens: list[str]) -> int:
    stack = []
    operators = {
        '+': lambda op1, op2: op1 + op2,
        '-': lambda op1, op2: op1 - op2,
        '*': lambda op1, op2: op1 * op2,
        '/': lambda op1, op2: int(op1 / op2)
    }
    for token in tokens:
        if token in operators:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(operators[token](op1, op2))
        else:
            stack.append(int(token))

    return stack[-1]
print(evalRPN_refactord(tokens = ["-2","4","/","2","-3","-","-"]))