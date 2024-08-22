def findComplement(num: int) -> int:
    bin_rep = bin(num)[2:]
    ans_bin_rep = ""

    for bit in bin_rep:
        ans_bin_rep += str((int(bit) ^ 1))
    
    ans_dec_rep = int("0b"+ans_bin_rep, base = 0)

    return ans_dec_rep

def findComplement_optimized(num: int) -> int:
    bits_length = len(bin(num)[2:])

    # The idea of creating the mask here is brillient, shift the 1 to the fourth position and then you can subtract 1 to reach the all ones mask
    mask = (1 << bits_length) - 1
    return num ^ mask

print(findComplement_optimized(5))
