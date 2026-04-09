from collections import defaultdict
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """    
                BFS with priority queue, not just FIFO Queue    
        points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
        pts: a, b, c, d, e
        BFS
        1. make adjs graph whose edge is the manhattan dist >> O(N**2) where N = len(points)
           adjs = {pt0: [(d1, pt1), (d2, pt2), ...]}
        2. pick one pt, mark it as visited, and push all it's neis to minHeap
        3. do BFS, but use priority queue, heapq, instead of the normal Queue, to choose the 
           closest nei with minimum dist cost.
        4. make sure to add to visited set, and check if already visited before considering a pt

        """
                # constructing adj graph
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                weight = abs(x1 - x2) + abs(y1 - y2)
                # make sure to add both ways, BIDIRECTIONAL, undirected graph
                adj[i].append((weight, j))
                adj[j].append((weight, i)) 
                
        minHeap, visited, minCost = [], set(), 0

        # pick any one of the point, mark it visited and push it's nei to minHeap 
        for wei, nei in adj[0]:
            heapq.heappush(minHeap, (wei, nei))
        visited.add(0)

        while len(visited) < len(points):
            weight, nei = heapq.heappop(minHeap)
            if nei in visited: continue
            minCost += weight
            visited.add(nei)
            for cost, nei2 in adj[nei]:
                if nei2 not in visited:
                    heapq.heappush(minHeap, (cost, nei2))
        
        return minCost

        
