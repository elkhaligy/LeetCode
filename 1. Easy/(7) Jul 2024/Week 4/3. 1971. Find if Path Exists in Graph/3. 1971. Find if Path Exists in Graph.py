from collections import defaultdict

def validPath_dfs_recursive(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    # Create adjacency list
    adj_list = defaultdict(list)
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    
    def dfs_recursive(adj_list, cur_node, visited):
        if cur_node == destination:
            return True
        visited.add(cur_node)
        for nei in adj_list[cur_node]:
            if nei not in visited:
                if dfs_recursive(adj_list, nei, visited):
                    return True
        return False

    visited = set()

    return dfs_recursive(adj_list, source, visited)


def validPath_dfs_iterative(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    # Create adjacency list
    adj_list = defaultdict(list)
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    def dfs_iterative(adj_list, source, visited):
        stack = [source]
        visited.add(source)

        while stack:
            cur_node = stack.pop()
            if cur_node == destination:
                return True
            for nei in adj_list[cur_node]:
                if nei not in visited:
                    stack.append(nei)
                    visited.add(nei)
        return False

    visited = set()

    return dfs_iterative(adj_list, source, visited)

print(validPath_dfs_iterative(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2))