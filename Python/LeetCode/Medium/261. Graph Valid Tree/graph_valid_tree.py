from typing import List

class Solution:
    """
    This class provides an implementation of the 'Graph Valid Tree' problem.

    A valid tree must:
    1. Have exactly `n - 1` edges (where `n` is the number of nodes).
    2. Be fully connected (i.e., no disconnected components).
    3. Contain no cycles.
    """

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Determines if the given graph forms a valid tree.

        :param n: Number of nodes (labeled 0 to n - 1)
        :param edges: List of undirected edges connecting nodes
        :return: True if the graph is a valid tree, False otherwise
        """
        if not n:
            return True     # An empty graph is technically a valid tree

        # Build adjacency list
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Depth-First Search (DFS) for cycle detection
        visit_set = set()

        def dfs(node, parent):
            if node in visit_set:
                return False                    # Cycle detected

            visit_set.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue                    # Ignore edge leading back to parent
                if not dfs(neighbor, node):
                    return False                # Found a cycle

            return True

        # The graph is a valid tree if:
        # 1. DFS confirms no cycles
        # 2. We visit all nodes (ensuring connectivity)
        return dfs(0, -1) and len(visit_set) == n


def main():
    """
    Demonstrates testing the graph validity function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]]),              # Expected output: True
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]),      # Expected output: False (Cycle detected)
        (4, [[0, 1], [2, 3]]),                              # Expected output: False (Disconnected graph)
        (1, []),                                            # Expected output: True (A single node with no edges is a valid tree)
    ]

    for n, edges in test_cases:
        print(f"n = {n}, edges = {edges}")
        result = solver.validTree(n, edges)
        print(f"Valid Tree? {result}\n")


if __name__ == "__main__":
    main()
