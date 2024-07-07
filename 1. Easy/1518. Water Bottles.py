def numWaterBottles_simulation_1(numBottles: int, numExchange: int) -> int:
    drink = 0
    empty_bottles = 0

    while numBottles:
        drink += numBottles
        empty_bottles += numBottles
        numBottles = empty_bottles // numExchange
        empty_bottles = empty_bottles % numExchange
    
    return drink

def numWaterBottles_simulation_2(numBottles: int, numExchange: int) -> int:
    answer = numBottles
    quotient = numBottles // numExchange
    remainder = numBottles % numExchange
    
    while quotient:
        answer += quotient
        empty_bottles = remainder + quotient
        remainder = empty_bottles % numExchange
        quotient =  empty_bottles // numExchange
       
    return answer


print(numWaterBottles_simulation_2(numBottles = 15, numExchange = 4))