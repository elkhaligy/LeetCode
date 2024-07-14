def averageWaitingTime(customers: list[list[int]]) -> float:
    prev_c = customers[0][0]
    prev_s = customers[0][0]
    prev_f = customers[0][1] + prev_s
    waiting = prev_f - prev_c 
    
    for customer in customers[1:]:
        come = customer[0]
        start = prev_f
        if start < come:
            start = come
        finish = customer[1] + start
        prev_f = finish
        waiting += finish - come

    return waiting / len(customers)

print(averageWaitingTime(customers = [[5,2],[5,4],[10,3],[20,1]]))