from typing import List

class Solution:
    def __init__(self):
        """
        Initializes the solution with parent and depth arrays.
        - `parent`: Tracks the representative (root) of each node's connected component.
        - `depth`: Stores the depth of each connected component to optimize union operations.
        """
        self.parent = []
        self.depth = []
    
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        Computes the minimum cost of walking from `s` to `t` in an undirected graph.

        :param n: Number of vertices labeled from 0 to n-1.
        :param edges: A list of edges where each edge is represented as [u, v, w].
                      - `u` and `v` are the connected vertices.
                      - `w` is the weight of the edge.
        :param queries: A list of queries where each query is [s, t].
                        - `s` is the start vertex.
                        - `t` is the end vertex.
        :return: A list of integers where each value is the minimum cost for the respective query.
        """
        self.parent = [-1] * n  # Initially, each node is its own parent (disjoint set)
        self.depth = [0] * n  # Tracks the depth of each component
        component_cost = [-1] * n  # Tracks the bitwise AND cost for each component

        # Step 1: Union-Find to connect components
        for u, v, _ in edges:
            self._union(u, v)

        # Step 2: Compute the bitwise AND cost for each component
        for u, v, w in edges:
            root = self._find(u)
            component_cost[root] &= w  # Update the cost by performing AND operation

        # Step 3: Process queries
        answer = []
        for s, t in queries:
            # If s and t are in different components, return -1
            if self._find(s) != self._find(t):
                answer.append(-1)
            else:
                # Return the precomputed AND cost of the component
                answer.append(component_cost[self._find(s)])

        return answer

    def _find(self, node: int) -> int:
        """
        Find function with path compression:
        - Returns the representative (root) of the set containing `node`.
        - Applies path compression to speed up future queries.

        :param node: The node whose root is to be found.
        :return: The root of the component.
        """
        if self.parent[node] == -1:
            return node
        self.parent[node] = self._find(self.parent[node])  # Path compression
        return self.parent[node]

    def _union(self, node1: int, node2: int) -> None:
        """
        Union function to merge two components using union by rank:
        - Ensures that the shallower tree is merged under the deeper one.

        :param node1: First node.
        :param node2: Second node.
        """
        root1 = self._find(node1)
        root2 = self._find(node2)

        if root1 == root2:
            return  # Already in the same component

        # Union by rank (depth)
        if self.depth[root1] < self.depth[root2]:
            root1, root2 = root2, root1  # Swap to ensure root1 is deeper

        self.parent[root2] = root1  # Merge root2 into root1

        if self.depth[root1] == self.depth[root2]:
            self.depth[root1] += 1  # Increment depth if both were equal

def main():
    """
    Driver function to test the `minimumCost` function with sample inputs.
    """
    solution = Solution()

    # Example test case 1
    n1 = 5
    edges1 = [[0, 1, 7], [1, 3, 7], [1, 2, 11]]
    queries1 = [[0, 3], [3, 4]]
    print(f"Test Case 1 Output: {solution.minimumCost(n1, edges1, queries1)}")

    # Example test case 2
    n2 = 3
    edges2 = [[0, 2, 15], [2, 1, 1]]
    queries2 = [[1, 2]]
    print(f"Test Case 2 Output: {solution.minimumCost(n2, edges2, queries2)}")

if __name__ == "__main__":
    main()
