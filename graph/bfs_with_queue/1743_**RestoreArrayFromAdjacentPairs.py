class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        """
        1. bidirectional adjs graph
        2. get either the START or the END node (the one with only one branch) and add to Queue
        3. BFS, and collect if not SEEN
        4. result could be START to END or END to START depending where we start

        """
        adjs = defaultdict(list)
        for a, b in adjacentPairs:
            adjs[a].append(b)
            adjs[b].append(a)

        for k, v in adjs.items():
            if len(v) == 1:
                start = k

        queue, result, seen = deque(), [], set()
        queue.append(start)
        while queue:
            num = queue.popleft()
            result.append(num)
            seen.add(num)
            for nei in adjs[num]:
                if nei not in seen:
                    queue.append(nei)
        return result

