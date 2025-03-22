from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Count the number of complete connected components in an undirected graph.

        A connected component is complete if every pair of vertices in the component is directly connected.

        :param n: Total number of vertices in the graph.
        :param edges: List of undirected edges, each represented by a list [u, v].
        :return: Number of complete connected components.
        """
        # Initialize adjacency list with self-loop for each node
        graph = [[] for _ in range(n)]
        for vertex in range(n):
            graph[vertex] = [vertex]

        # Build graph connections
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Count frequency of identical neighbor sets
        component_freq = defaultdict(int)
        for vertex in range(n):
            neighbors = tuple(sorted(graph[vertex]))
            component_freq[neighbors] += 1

        # A component is complete if the number of neighbors == frequency of that neighbor pattern
        complete_count = sum(
            1
            for neighbors, freq in component_freq.items()
            if len(neighbors) == freq
        )

        return complete_count

def main():
    sol = Solution()

    test_cases = [
        (6, [[0, 1], [0, 2], [1, 2], [3, 4]], 3),
        (6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]], 1),
    ]

    for i, (n, edges, expected) in enumerate(test_cases, 1):
        result = sol.countCompleteComponents(n, edges)
        print(f"Test Case {i}: Output = {result}, Expected = {expected}, Passed = {result == expected}")

if __name__ == "__main__":
    main()
