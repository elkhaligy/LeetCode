from collections import defaultdict

def countOfAtoms(formula: str) -> str:
    # We need to make a stack of dictionaries
    stack = [defaultdict(int)]
    index = 0

    while index < len(formula):
        # If left parenthesis, insert a new hashmap to the stack. It will
        # keep track of the atoms and their counts in the nested formula
        if formula[index] == "(":
            stack.append(defaultdict(int))
            index += 1

        # If right parenthesis, pop the top element from the stack
        # Multiply the count with the multiplicity of the nested formula
        elif formula[index] == ")":
            curr_map = stack.pop()
            index += 1
            multiplier = ""
            while index < len(formula) and formula[index].isdigit():
                multiplier += formula[index]
                index += 1
            if multiplier:
                multiplier = int(multiplier)
                for atom in curr_map:
                    curr_map[atom] *= multiplier

            for atom in curr_map:
                stack[-1][atom] += curr_map[atom]

        # Otherwise, it must be a UPPERCASE LETTER. Extract the complete
        # atom with frequency, and update the most recent hashmap
        else:
            # Extract atom name
            curr_atom = formula[index]
            index += 1
            while index < len(formula) and formula[index].islower():
                curr_atom += formula[index]
                index += 1

            # Extract atom number if exist
            curr_count = ""
            while index < len(formula) and formula[index].isdigit():
                curr_count += formula[index]
                index += 1

            # Add it to the top dictionary on the stack
            if curr_count == "":
                stack[-1][curr_atom] += 1
            else:
                stack[-1][curr_atom] += int(curr_count)

    # Sort the final map
    final_map = dict(sorted(stack[0].items()))

    # Generate the answer string
    ans = ""
    for atom in final_map:
        ans += atom
        if final_map[atom] > 1:
            ans += str(final_map[atom])

    return ans

print(countOfAtoms(formula = "Mg(OH)2"))