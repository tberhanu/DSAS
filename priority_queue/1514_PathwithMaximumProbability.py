from collections import defaultdict
import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        """
        from START to END => max prob

        """
        adj = defaultdict(list)
        for p, nodes in zip(succProb, edges):
            adj[nodes[0]].append((p, nodes[1]))
            adj[nodes[1]].append((p, nodes[0]))

        maxHeap, seen = [], set()
        heapq.heappush(maxHeap, (-1, start_node))

        while maxHeap:
            prob, end = heapq.heappop(maxHeap)
            if end in seen: continue
            seen.add(end)
            if end == end_node:
                return -prob
            # neis
            for prob2, end2 in adj[end]:
                if end2 not in seen:
                    heapq.heappush(maxHeap, (prob * prob2, end2)) # pos * neg == neg

        return 0

