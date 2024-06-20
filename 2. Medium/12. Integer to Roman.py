def intToRoman(num: int) -> str:
    roma_dict = {
        'I' : 1,
        'IV': 4,
        'V' : 5,
        'IX': 9,
        'X' : 10,
        'XL': 40,
        'L' : 50,
        'XC': 90,
        'C' : 100,
        'CD': 400,
        'D' : 500,
        'CM': 900,
        'M' : 1000
    }
    result = ""

    remainder = num
    while remainder:
        for item, value in roma_dict.items():
            if remainder - value < 0:
                break
            cur_symbol = item
            cur_value = value
        result += cur_symbol
        remainder -= cur_value
        if remainder == 0:
            break
    return result
# VII
intToRoman(1994)