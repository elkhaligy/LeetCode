from collections import defaultdict
import heapq

# It worked!, is there a better way to handle letters as letters instead of converting them to numbers? to be continued..
def minimumCost(source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:

    def dijkstra(adj_lst, shrt_pth_mat, node, node_to_num, num_to_node):
        priority_queue = [(0, node)]
        shortest_path_distances = shrt_pth_mat[node]

        while priority_queue:
            cur_distance, cur_city = heapq.heappop(priority_queue)
            if cur_distance > shortest_path_distances[cur_city]:
                continue
            for neighbor, weight in adj_lst[num_to_node[cur_city]]:
                if shortest_path_distances[node_to_num[neighbor]] > cur_distance + weight:
                    shortest_path_distances[node_to_num[neighbor]] = cur_distance + weight

                    heapq.heappush(priority_queue,(shortest_path_distances[node_to_num[neighbor]], node_to_num[neighbor]))
    
    # Some essential variables
    nodes_num = len(set(original + changed))
    nodes = list(set(original + changed))
    nodes_to_num_dict = {}
    num_to_nodes_dict = {}
    for i, node in enumerate(nodes):
        nodes_to_num_dict[node] = i
    for i, node in enumerate(nodes):
        num_to_nodes_dict[i] = node

    # Create adjacency list
    adj_lst = defaultdict(list)
    for org, chan, cst in zip(original, changed, cost):
        adj_lst[org].append((chan, cst))
    
    # Apply dijsktra algorithm
    shrt_pth_mat = [[float('inf') for _ in range(nodes_num)] for _ in range(nodes_num)]
    for node in range(nodes_num):
        shrt_pth_mat[node][node] = 0
    for node in nodes:
        dijkstra(adj_lst, shrt_pth_mat, nodes_to_num_dict[node],nodes_to_num_dict ,num_to_nodes_dict)

    #     c  e   a   b   d
    # c [[0, 1, inf, 3, inf], 
    # e  [7, 0, inf, 2, inf], 
    # a  [7, 8, 0, 2, inf], 
    # b  [5, 6, inf, 0, inf], 
    # d [27, 20, inf, 22, 0]]

    # Calculate answer easily using the shortest path matrix
    ans = 0
    for c1, c2 in zip(source, target):
   
        if shrt_pth_mat[nodes_to_num_dict[c1]][nodes_to_num_dict[c2]] == float('inf'):
            return -1
        ans += shrt_pth_mat[nodes_to_num_dict[c1]][nodes_to_num_dict[c2]] 
    return ans



print(minimumCost(source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]))