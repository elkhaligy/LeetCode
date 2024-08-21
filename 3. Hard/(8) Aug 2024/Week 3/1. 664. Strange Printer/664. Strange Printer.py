def strangePrinter_top_down(s: str) -> int:

    """This function takes a string, start index and end index then returns the number of turns needed to print this string
    Args:
        string (str): The string to operate on
        start (int): Starting index
        end (int): Ending index
    Returns:
        int: Minimum number of turns to print that string
    """    
    def minimum_turns(string: str, start: int, end: int) -> int:
        if start > end:
            return 0
        min_turns = 1 + minimum_turns(string, start + 1, end)

        for i in range(start + 1, end + 1):
            if string[i] == string[start]:
                turns_with_match = minimum_turns(string, start, i - 1) + minimum_turns(string, i + 1, end)
                min_turns = min(min_turns, turns_with_match)
        
        return min_turns
    
    return minimum_turns(s, 0, len(s) - 1)

def strangePrinter_memoization(s: str) -> int:
    # Note: To optimize the solution further, we can remove consecutive duplicates
    memo = {} # A memoization dictionary that holds (start: int, end: int) : minimum turns: int

    """This function takes a string, start index and end index then returns the number of turns needed to print this string
    Args:
        string (str): The string to operate on
        start (int): Starting index
        end (int): Ending index
    Returns:
        int: Minimum number of turns to print that string
    """    
    def minimum_turns(string: str, start: int, end: int) -> int:
        # Base case, if start index exceeded end index then minimum turns is 0
        if start > end:
            return 0
        # Memoization technique to speed up the process
        if (start, end) in memo:
            return memo[(start, end)]

        # Worst case, a turn for each character
        min_turns = 1 + minimum_turns(string, start + 1, end)

        # Optimized case, if the first char match the last char
        for i in range(start + 1, end + 1):
            if string[i] == string[start]:
                turns_with_match = minimum_turns(string, start, i - 1) + minimum_turns(string, i + 1, end)
                min_turns = min(min_turns, turns_with_match)

        # Update memoization dictionary with the min value
        memo[(start, end)] = min_turns
        return min_turns
    
    return minimum_turns(s, 0, len(s) - 1)

print(strangePrinter_memoization("cabad"))