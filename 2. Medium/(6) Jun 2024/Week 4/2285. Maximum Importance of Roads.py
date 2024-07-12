def maximumImportance_sol1(n: int, roads: list[list[int]]) -> int:
    node_degree = [0] * n # index: node number, value: node degree

    for edge in roads:
        node_degree[edge[0]] += 1
        node_degree[edge[1]] += 1
    
    node_degree_pairs = []
    for node, degree in enumerate(node_degree):
        node_degree_pairs.append((node, degree))
    node_degree_pairs.sort(key= lambda x: x[1])

    answer = 0
    num = 1
    for pair in node_degree_pairs:
        answer += num * pair[1]
        num += 1
    #print(node_degree_pairs)
    return answer

def maximumImportance_sol2(n: int, roads: list[list[int]]) -> int:
    node_degree = [0] * n # index: node number, value: node degree

    for edge in roads:
        node_degree[edge[0]] += 1
        node_degree[edge[1]] += 1

    node_degree.sort()

    answer = 0
    num = 1
    
    for degree in node_degree:
        answer += degree * num
        num += 1

    return answer
print(maximumImportance_sol2(n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
