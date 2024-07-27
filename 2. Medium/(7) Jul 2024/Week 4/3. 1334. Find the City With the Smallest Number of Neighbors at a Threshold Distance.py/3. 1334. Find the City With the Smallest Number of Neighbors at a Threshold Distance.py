from collections import defaultdict
import heapq
class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        # Create adjacency list for undirected graph
        adj_lst = defaultdict(list)
        for start, end, weight in edges:
            adj_lst[start].append((end, weight))
            adj_lst[end].append((start, weight))
        # print(adj_lst)

        # Create shorted path matrix n * n where rows are nodes and columns are nodes and their intersection gives the shorted path from the node in row to the node in column
        shrt_pth_mat = [[float('inf') for _ in range(n)] for _ in range(n)]
        for node in range(n):
            shrt_pth_mat[node][node] = 0
        
        # Populate the shortes path matrix using dijkstra algorithm
        for node in range(n):
            self.dijkstra(adj_lst, shrt_pth_mat, node)
        
        # print(shrt_pth_mat)
        #       0  1  2  3 
        #   0 [[0, 3, 4, 5], 
        #   1  [3, 0, 1, 2], 
        #   2  [4, 1, 0, 1], 
        #   3  [5, 2, 1, 0]]
        
        # Now that we have the shortest path n x n matrix, it is easy to get the answer
        min_reachable_counter = float('inf')
        min_city = 0
        for i in range(n):
            cur_reachable = 0
            for j in range(n):
                if shrt_pth_mat[i][j] > 0 and shrt_pth_mat[i][j] <= distanceThreshold:
                    cur_reachable += 1
            
            if cur_reachable <= min_reachable_counter:
                min_reachable_counter = cur_reachable
                min_city = i
            
        return min_city
    def dijkstra(self, adj_lst, shrt_pth_mat, node):
        n = len(shrt_pth_mat)
        priority_queue = [(0, node)]
        shortest_path_distances = shrt_pth_mat[node]

        while priority_queue:
            cur_distance, cur_city = heapq.heappop(priority_queue)
            if cur_distance > shortest_path_distances[cur_city]:
                continue
            for neighbor, weight in adj_lst[cur_city]:
                if shortest_path_distances[neighbor] > cur_distance + weight:
                    shortest_path_distances[neighbor] = cur_distance + weight

                    heapq.heappush(priority_queue,(shortest_path_distances[neighbor], neighbor),)