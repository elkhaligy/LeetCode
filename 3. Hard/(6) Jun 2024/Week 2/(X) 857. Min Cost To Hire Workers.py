def mincostToHireWorkers(quality: list[int], wage: list[int], k: int) -> float:
    q_per_w = [item1/item2 for item1, item2 in zip(quality,wage)]
    #print(q_per_w)

    # Sorting quality based on quality per wage
    temp = sorted(zip(q_per_w, quality), reverse=True)
    keys, vals = zip(*temp)
    quality = list(vals)
    print(quality)

    # Sorting wage based on quality per wage
    temp = sorted(zip(q_per_w, wage), reverse=True)
    keys, vals = zip(*temp)
    wage = list(vals)
    print(wage)

    # Start chosing k groups and test them
    ans = float('inf')
    for i in range(len(quality)):
        group_quality = quality[i: i + k - 1 + 1]
        group_wage = wage[i: i + k - 1 + 1]
        print(f"group quality:  {group_quality if len(group_quality) == k else ''}")
        print(f"group wage:  {group_wage if len(group_quality) == k else ''}")
        # Start calculating cost for each group
        if len(group_quality) == k:
            min_quality = min(group_quality)
            max_quality = max(group_quality)
            min_quality_index = group_quality.index(min_quality)
            max_quality_index = group_quality.index(max_quality)
            min_wage = group_wage[min_quality_index]
            max_wage = max(group_wage[max_quality_index], max(group_wage))

            for index, qual in enumerate(group_quality):
                group_wage[index] = max(group_wage[index], qual/min_quality * min_wage)
            
            for index, qual in enumerate(group_quality):
                group_wage[index] = max(group_wage[index], qual/max_quality * max_wage)
            
            print(f"fixed group wage:  {group_wage}")
            
            ans = min(ans, sum(group_wage))    
            print(f"ans:  {ans}")
    return ans

def mincostToHireWorkers_Sol2(quality: list[int], wage: list[int], k: int) -> float:
    wages_temp = wage[:]
    ans_list = []
    for index, captain_quality in enumerate(quality):
        # offer(index) = quality(index) * (offer(captain) / quality(captain))
        for index2, others_quality in enumerate(quality):
            offered_wage = others_quality * (wage[index] / captain_quality)
            if offered_wage < wage[index2]:
                wages_temp[index2] = -1
            else:
                wages_temp[index2] = offered_wage
        ans_list.append([item for item in wages_temp if item != -1])
        #print(wages_temp)
    
    #print(ans_list)
    sums_lst = []
    for lst in ans_list:
        if len(lst) >= k:
            lst.sort()
            sums_lst.append(sum(lst[:k]))
    
    return min(sums_lst)





print(mincostToHireWorkers_Sol2(quality = [10,20,5], wage = [70,50,30], k = 2))