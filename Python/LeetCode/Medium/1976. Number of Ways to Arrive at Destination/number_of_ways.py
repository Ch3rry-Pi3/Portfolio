from heapq import heappop, heappush
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        Returns the number of different ways to reach node n-1 from node 0
        using paths that take the shortest possible time.

        :param n: Number of intersections (nodes)
        :param roads: List of roads represented as [u, v, time]
        :return: Number of shortest-time paths from node 0 to node n-1 (modulo 1e9+7)
        """
        MOD = 1_000_000_007

        # Build graph as an adjacency list
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Dijkstra's algorithm using a min heap
        heap = [(0, 0)]  # (time, node)
        shortest_time = [float('inf')] * n
        path_count = [0] * n
        shortest_time[0] = 0
        path_count[0] = 1

        while heap:
            curr_time, node = heappop(heap)
            if curr_time > shortest_time[node]:
                continue

            for neighbor, time in graph[node]:
                total_time = curr_time + time

                # If a shorter path is found
                if total_time < shortest_time[neighbor]:
                    shortest_time[neighbor] = total_time
                    path_count[neighbor] = path_count[node]
                    heappush(heap, (total_time, neighbor))

                # If another shortest path is found
                elif total_time == shortest_time[neighbor]:
                    path_count[neighbor] = (path_count[neighbor] + path_count[node]) % MOD

        return path_count[n - 1]


def main():
    solution = Solution()

    test_cases = [
        (
            7,
            [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1],
             [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]],
            4
        ),
        (
            2,
            [[1, 0, 10]],
            1
        )
    ]

    for i, (n, roads, expected) in enumerate(test_cases):
        result = solution.countPaths(n, roads)
        print(f"Test Case {i + 1}: Output = {result}, Expected = {expected}")
        assert result == expected, "❌ Test failed!"
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
