class Solution:
    def maxNumEdgesToRemove_TLE(self, n: int, edges: list[list[int]]) -> int:
        result = 0
        e1 = e2 = 0

        # Alice and Bob
        parent = list(range(n + 1))
        for type, node1, node2 in edges:
            if type == 3:
                if self.find_parent(node1, parent) == self.find_parent(node2, parent):
                    result += 1
                else:
                    e1 += 1
                    e2 += 1
                    self.union(node1, node2, parent)
        #print(f"Type 3 Result: {result}")

        # Alice
        alice_parent = parent[:]
        for type, node1, node2 in edges:
            if type == 1:
                if self.find_parent(node1, alice_parent) == self.find_parent(node2, alice_parent):
                    result += 1
                else:
                    e1 += 1
                    self.union(node1, node2, alice_parent)
        #print(f"Type 1 Result: {result}")

        # Bob
        bob_parent = parent[:]
        for type, node1, node2 in edges:
            if type == 2:
                if self.find_parent(node1, bob_parent) == self.find_parent(node2, bob_parent):
                    result += 1
                else:
                    e2 += 1
                    self.union(node1, node2, bob_parent)

        #print(f"Type 2 Result: {result}")
        return result if e1 == e2 == n - 1 else -1

    def find_parent(self, node: int, parent: list[int]):
        while parent[node] != node:
            node = parent[node]

        return node

    def union(self, node1: int, node2: int, parent: list[int]):
        parent1 = self.find_parent(node1, parent)
        parent2 = self.find_parent(node2, parent)

        if parent1 != parent2:
            parent[parent2] = parent1


    def maxNumEdgesToRemove_ac(self, n: int, edges: list[list[int]]) -> int:

        def find_parent(node: int):
            # Whats the difference here?

            # while parent[node] != node:
            #     node = parent[node]

            # return node
            if node != parent[node]:
                parent[node] = find_parent(parent[node])
            return parent[node]

        def union(node1: int, node2: int):
            parent1 = find_parent(node1)
            parent2 = find_parent(node2)

            if parent1 != parent2:
                parent[parent2] = parent1
                return 1
            else:
                return 0

        result = 0
        e1 = e2 = 0
        
        # Alice and Bob
        parent = list(range(n + 1))
        for type, node1, node2 in edges:
            if type == 3:
                if union(node1, node2):
                    e1 += 1
                    e2 += 1
                else:
                    result += 1
        #print(f"Type 3 Result: {result}")

        # Alice
        parent_backup = parent[:]
        for type, node1, node2 in edges:
            if type == 1:
                if union(node1, node2):
                    e1 += 1
                else:
                    result += 1
        #print(f"Type 1 Result: {result}")

        # Bob
        parent = parent_backup[:]
        for type, node1, node2 in edges:
            if type == 2:
                if union(node1, node2):
                    e2 += 1
                else:
                    result += 1

        #print(f"Type 2 Result: {result}")
        return result if e1 == e2 == n - 1 else -1
    
sol_obj = Solution()
print(sol_obj.maxNumEdgesToRemove_ac(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))

