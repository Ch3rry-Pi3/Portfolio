from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        """
        Returns the minimum distance from node s to any marked node using Dijkstra's algorithm.
        """
        mark_set = set(marked)
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))

        dist = {s: 0}
        min_heap = [(0, s)]

        while min_heap:
            distance, node = heapq.heappop(min_heap)

            if node in mark_set:
                return dist[node]

            for next_node, weight in adj[node]:
                new_dist = distance + weight
                if new_dist < dist.get(next_node, float("inf")):
                    dist[next_node] = new_dist
                    heapq.heappush(min_heap, (new_dist, next_node))

        return -1


def main():
    solution = Solution()
    test_cases = [
        # (n, edges, s, marked, expected)
        (4, [[0, 1, 1], [1, 2, 3], [2, 3, 2], [0, 3, 4]], 0, [2, 3], 4),
        (5, [[0, 1, 2], [0, 2, 4], [1, 3, 1], [2, 3, 3], [3, 4, 2]], 1, [0, 4], 3),
        (4, [[0, 1, 1], [1, 2, 3], [2, 3, 2]], 3, [0, 1], -1),
    ]

    for n, edges, s, marked, expected in test_cases:
        result = solution.minimumDistance(n, edges, s, marked)
        print(f"Input: n={n}, s={s}, marked={marked}\nEdges: {edges}\nExpected: {expected}, Got: {result}\n")


if __name__ == "__main__":
    main()
