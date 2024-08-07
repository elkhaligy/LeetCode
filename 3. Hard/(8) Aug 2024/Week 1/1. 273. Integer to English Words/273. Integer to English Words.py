# Solved successfully, but a note:
# The output was correct but the between the words were wrong, if you had though of the spaces logic
# carefully on the board, you wouldn't have spent that much time on debugging the wrong space
# so for each piece of logic even if it is small, you need to draw it on the board to write a bug free code 
equi_dict = {
    0 : "",
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five",
    6 : "Six",
    7 : "Seven",
    8 : "Eight",
    9 : "Nine",
    10 : "Ten",
    11 : "Eleven",
    12 : "Twelve",
    13 : "Thirteen",
    14 : "Fourteen",
    15 : "Fifteen",
    16 : "Sixteen",
    17 : "Seventeen",
    18 : "Eighteen",
    19 : "Nineteen",
    20 : "Twenty",
    30 : "Thirty",
    40 : "Forty",
    50 : "Fifty",
    60 : "Sixty",
    70 : "Seventy",
    80 : "Eighty",
    90 : "Ninety",
    100 : "Hundred",
    1000 : "Thousand",
    1000000 : "Million",
    1000000000 : "Billion"
}

def numberToWords(num: int) -> str:
    if num == 0:
        return "Zero"
    
    ans = ""
    
    # Normalize the number with additional zeros inorder to make it divisible by 3
        # For example if given 12 it will be 012
    nums_arr = list(str(num))
    while len(nums_arr) % 3 != 0:
        nums_arr.insert(0, "0")
    nums = "".join(nums_arr)
    n = len(nums)

    # Start applying the algorithm
    for i in range(0, n - 2, 3):
        # Start extracting current group
        cur_group = ""
        cur_group += nums[i]
        cur_group += nums[i + 1]
        cur_group += nums[i + 2]
            
        if int(cur_group) == 0: # If current group is zero, then nothing needs to be done
            continue
        #print(cur_group)

        # Identify to which category this group is (billion, million, thousand)
        category_identifier_num = int(cur_group)
        for _ in range(n - 1 - i - 2):
            category_identifier_num *= 10
        group = ""
        if category_identifier_num >= 1_000_000_000 and category_identifier_num <= 999_999_999_999:
            group = "Billion"
        elif category_identifier_num >= 1_000_000 and category_identifier_num <= 999_999_999:
            group = "Million"
        elif category_identifier_num >= 1_000 and category_identifier_num <= 999_999:
            group = "Thousand"

        # Start applying the helper function and construct the answer
        current_str = helper(cur_group, len(ans))
        ans += current_str
        ans += " "
        ans += group

    return ans.strip()
    
def helper(nums: str, ans_len: int):
    ans = ""
    # If answer len is not 0, then we need to add a space before the current group answer
    if ans_len != 0:
        ans += " "

    # Extract hundreds, tens and ones from the current group
    hundreds = int(nums[0])
    tens     = int(nums[1])
    ones     = int(nums[2])

    # Apply the logic to construct the answer
    if hundreds != 0:
        ans += equi_dict[hundreds]
        ans += " "
        ans += "Hundred"

    if tens != 0:
        if hundreds != 0:
            ans += " "

        if tens * 10 + ones < 20:
            ans += equi_dict[tens * 10 + ones]
        else:
            ans += equi_dict[tens * 10]
            if ones != 0:
                ans += " "
                ans += equi_dict[ones]
    elif ones != 0:
        if hundreds != 0:
            ans += " "
        ans += equi_dict[ones]

    return ans
    

print(numberToWords(50868))


