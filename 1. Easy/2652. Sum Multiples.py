class Solution:
    def sumOfMultiples_oN(self, n: int) -> int:
        answer = 0

        for num in range(1, n + 1):
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                answer += num
        
        return answer
    def sumOfMultiples_o1(self, n: int) -> int:
        def sum_of_numbers_divisible_by_k(k: int):
            return k * (n // k) * ((n // k) + 1) // 2
        
        return sum_of_numbers_divisible_by_k(3) + sum_of_numbers_divisible_by_k(5) +\
               sum_of_numbers_divisible_by_k(7) - sum_of_numbers_divisible_by_k(3 * 5) -\
               sum_of_numbers_divisible_by_k(3 * 7) - sum_of_numbers_divisible_by_k(5 * 7) +\
               sum_of_numbers_divisible_by_k(3 * 5 * 7)
            


    
sol_obj = Solution()
print(sol_obj.sumOfMultiples_o1(n= 7))