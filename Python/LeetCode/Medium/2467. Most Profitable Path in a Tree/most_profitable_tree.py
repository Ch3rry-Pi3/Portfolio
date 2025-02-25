from typing import List

class Solution:
    def __init__(self):
        """
        Initialises the tree structure and distance tracking.
        """
        self.tree = []
        self.distance_from_bob = []
        self.n = 0

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        """
        Computes the most profitable path Alice can take.
        
        :param edges: List[List[int]] - The edge list representing the tree.
        :param bob: int - The starting node of Bob.
        :param amount: List[int] - The income or cost at each node.
        :return: int - Maximum net income Alice can achieve.
        """
        self.n = len(amount)
        self.tree = [[] for _ in range(self.n)]
        self.distance_from_bob = [0] * self.n

        # Build adjacency list representation of the tree
        for edge in edges:
            self.tree[edge[0]].append(edge[1])
            self.tree[edge[1]].append(edge[0])

        return self._find_paths(0, 0, 0, bob, amount)

    def _find_paths(self, source: int, parent: int, time: int, bob: int, amount: List[int]) -> int:
        """
        DFS to find maximum income path.
        
        :param source: int - Current node in traversal.
        :param parent: int - Parent node in traversal.
        :param time: int - Current time step.
        :param bob: int - Bob's initial position.
        :param amount: List[int] - List of values at each node.
        :return: int - Maximum net income from this node.
        """
        max_income = 0
        max_child = float("-inf")

        # Compute distances from Bob
        if source == bob:
            self.distance_from_bob[source] = 0
        else:
            self.distance_from_bob[source] = self.n

        # Explore child nodes
        for neighbor in self.tree[source]:
            if neighbor != parent:
                max_child = max(
                    max_child,
                    self._find_paths(neighbor, source, time + 1, bob, amount),
                )
                self.distance_from_bob[source] = min(
                    self.distance_from_bob[source],
                    self.distance_from_bob[neighbor] + 1,
                )

        # Compute income based on Alice and Bob's arrival times
        if self.distance_from_bob[source] > time:
            max_income += amount[source]            # Alice gets full amount
        elif self.distance_from_bob[source] == time:
            max_income += amount[source] // 2       # Split reward

        return max_income if max_child == float("-inf") else max_income + max_child


def main():
    """
    Runs a sample test case.
    """
    solution = Solution()

    edges = [[0,1],[1,2],[1,3],[3,4]]
    bob = 3
    amount = [-2,4,2,-4,6]

    print(solution.mostProfitablePath(edges, bob, amount))          # Output: 6


if __name__ == "__main__":
    main()
