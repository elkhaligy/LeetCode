def findCenter_oN(edges: list[list[int]]) -> int:
    n = len(edges)
    # key - > node : value - > it's edges
    degree_counter = {}

    for edge in edges:
        node_1 = edge[0]
        node_2 = edge[1]
        degree_counter[node_1] = degree_counter.get(node_1, 0) + 1
        degree_counter[node_2] = degree_counter.get(node_2, 0) + 1
        if degree_counter[node_1] == n:
            return node_1
        if degree_counter[node_2] == n:
            return node_2