def max_parts(labels):
    last_occr_dct = {}
    partitions = []

    for i in range(len(labels) - 1, -1, -1):
        if labels[i] in last_occr_dct:
            continue
        else:
            last_occr_dct[labels[i]] = i
    
    i = 0
    # while i < len(labels):
    #     start = i
    #     end = last_occr_dct[labels[i]]
    #     j = 0
    #     while j != end:
    #         if last_occr_dct[labels[j]] > end:
    #             end = last_occr_dct[labels[j]]
    #         j += 1
    #     i = end + 1
    #     partitions.append(labels[start:end + 1])
    end = 0
    prev_start = 0
    for i in range(len(labels)):
        start = i
        end = max(last_occr_dct[labels[start]], end)

        if i == end:
            partitions.append(labels[prev_start: end + 1])
            prev_start = i + 1
            
        print(start, end)

    #print(partitions)
    return [len(item) for item in partitions]


print(max_parts('ababcbacadefegdehijhklij'))