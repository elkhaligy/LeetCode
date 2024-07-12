class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        print(parent)

        for edge in edges:
            if self.find_parent(edge[0], parent) == self.find_parent(edge[1], parent):
                return edge
            self.union(edge[0], edge[1], parent)

        return None
    
    def find_parent(self, node: int, parent: list[int]):
        while parent[node] != node:
            node = parent[node]

        return node

    def union(self, node1: int, node2: int, parent: list[int]):
        parent1 = self.find_parent(node1, parent)
        parent2 = self.find_parent(node2, parent)

        if parent1 != parent2:
            parent[parent2] = parent1


sol_obj = Solution()
print(sol_obj.findRedundantConnection(edges = [[1,4],[3,4],[1,3],[1,2],[4,5]]))




