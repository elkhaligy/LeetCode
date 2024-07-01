def getAncestors(n: int, edges: list[list[int]]) -> list[list[int]]:
    reversed_adj_list = [[] for _ in range(n)]

    for edge in edges:
        reversed_adj_list[edge[1]].append(edge[0])

    print(reversed_adj_list)
    ancestors_list = []

    for node in range(n):
        cur_ancestors = []
        visited = set()
        dfs(node, reversed_adj_list, visited)

        for cur_node in range(n):
            if cur_node == node:
                continue
            if cur_node in visited:
                cur_ancestors.append(cur_node)
        ancestors_list.append(cur_ancestors)

    return ancestors_list

def dfs(node: int, reversed_adj_list: list[list[int]], visited: set) -> None:
    visited.add(node)

    for neighbour in reversed_adj_list[node]:
        if neighbour not in visited:
            dfs(neighbour, reversed_adj_list, visited)

print(getAncestors(n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))