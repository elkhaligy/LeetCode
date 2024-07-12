def reverseBits(n: int) -> int:
    bin_num = bin(n)[2:]
    bin_num_rev = bin_num[::-1]
    if len(bin_num_rev) < 32:
        bin_num_rev = bin_num_rev + "0" * (32 - len(bin_num_rev)) 

    return int(bin_num_rev, 2)


print(reverseBits(43261596))