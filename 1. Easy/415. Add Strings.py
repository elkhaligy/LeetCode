import sys

def addStrings_builtin(num1: str, num2: str) -> str:
    sys.set_int_max_str_digits(0)
    return str(int(num1) + int(num2))

def addStrings_sol1(num1: str, num2: str) -> str:
    num1_list = list(map(int, list(num1[::-1])))
    num2_list = list(map(int, list(num2[::-1])))
    larger = num1_list if len(num1_list) > len(num2_list) else num2_list
    smaller = num1_list if larger != num1_list else num2_list 
    #print(smaller)
    #print(larger)
    
    result = []
    for i in range(len(larger)):
        if i < len(smaller):
            result.append(larger[i] + smaller[i])
            print(larger[i] + smaller[i])
        else:
            result.append(larger[i])
    #print(result)
    tens = 0
    for i in range(len(result)):
        result[i] += tens
        tens = 0
        while result[i] >= 10:
            result[i] -= 10
            tens += 1
    if tens > 0:
        result.append(tens)
    return "".join(str(num) for num in result[::-1])


def addStrings_sol2(num1: str, num2: str) -> str:
    sys.set_int_max_str_digits(0)
    def str_to_int(num: str) -> int:
            converter_dict = {
                        '0' : 0, 
                        '1' : 1, 
                        '2' : 2, 
                        '3' : 3, 
                        '4' : 4, 
                        '5' : 5,
                        '6' : 6, 
                        '7' : 7, 
                        '8' : 8, 
                        '9' : 9
                    }
            
            output = 0
            for c in num:
                output = output * 10 + converter_dict[c]

            return output
    result = str_to_int(num1) + str_to_int(num2)
    return str(str_to_int(num1) + str_to_int(num2)) 

print(addStrings_sol2("123", "123"))