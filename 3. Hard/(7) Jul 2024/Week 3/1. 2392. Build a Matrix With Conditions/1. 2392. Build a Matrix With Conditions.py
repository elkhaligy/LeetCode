def buildMatrix(k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
    # Solved using topological sorting with dfs
    
    def dfs(src, graph, visited, curr_path, ans):
        if src in curr_path:
            return False

        if src in visited:
            return True
        
        visited.add(src)
        curr_path.add(src)

        for nei in graph.get(src, []):
            if not dfs(nei, graph, visited, curr_path, ans):
                return False
            
        curr_path.remove(src)
        ans.append(src)

        return True

    def topological_sort(edges: list[list[int]]) -> list[int]:
        # Creation of the adjacency list
        graph = {} # source node: [dst node 1, dst node2, ..]
        for src, dst in edges:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = []
                graph[src].append(dst)

        #print(f"Graph = {graph}")

        visited: set[int] = set()
        curr_path: set[int] = set()
        ans: list[int] = []

        for src in range(1, k + 1):
            if not dfs(src, graph, visited, curr_path, ans):
                return []
        
        return ans[::-1]
    
    rows = topological_sort(rowConditions)
    cols = topological_sort(colConditions)

    if len(rows) == 0 or len(cols) == 0:
        return []
    #print(f"Rows = {rows}, Cols = {cols}")

    pos_dict = {}

    for i, val in enumerate(rows):
        pos_dict[val] = []
        pos_dict[val].append(i)

    for i, val in enumerate(cols):
        pos_dict[val].append(i)
    #print(f"Positions Dictionary = {pos_dict}")

    result = [[0 for _ in range(k)] for _ in range(k)]

    for key, val in pos_dict.items():
        result[val[0]][val[1]] = key

    return result
print(buildMatrix(k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]))