from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        [course, prereq]
        1. adj graph
        2. collect independent courses in queue
        3. pop indep course, and traverse thru it's adj courses, update adj, add to queue
        4. when pop, count ++ 1
        4. when queue empty, if count == numCourses, True

        """
        lookup_num_prereqs = defaultdict(int)
        lookup_following_courses = defaultdict(list)
        queue = deque()

        for course, prereq in prerequisites:
            lookup_following_courses[prereq].append(course)
            lookup_num_prereqs[course] += 1
        
        for course in range(numCourses):
            if lookup_num_prereqs[course] == 0:
                queue.append(course)
        
        count = 0
        while queue:
            indep = queue.popleft()
            count += 1
            for next_course in lookup_following_courses[indep]:
                lookup_num_prereqs[next_course] -= 1
                if lookup_num_prereqs[next_course] == 0:
                    queue.append(next_course)
                    
        return count == numCourses
    
    # Only the below change needed to solve for:     210. Course Schedule II
        # orderings = []
        # while queue:
        #     indep = queue.popleft()
        #     orderings.append(indep)
        #     for next_course in lookup_following_courses[indep]:
        #         lookup_num_prereqs[next_course] -= 1
        #         if lookup_num_prereqs[next_course] == 0:
        #             queue.append(next_course)
                    
        # return [] if len(orderings) != numCourses else orderings

