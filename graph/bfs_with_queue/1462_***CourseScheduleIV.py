from collections import defaultdict
from typing import List
from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
    prerequisites[i] = [ai, bi] => must take course ai first if you want to take course bi.
    If [a, b] and [b, c], then [a, c]

        """
        prereq_to_courses = defaultdict(set)
        course_to_prereqs = defaultdict(set)
        lookup_prereq_counts = defaultdict(int)
        independents = deque()

        for prereq, course in prerequisites:
            prereq_to_courses[prereq].add(course)
            course_to_prereqs[course].add(prereq)
            lookup_prereq_counts[course] += 1

        for course in range(numCourses):
            if lookup_prereq_counts[course] == 0:
                independents.append(course)

        while independents:
            prereq = independents.pop()
            for course in prereq_to_courses[prereq]:
                indirect_prereqs = course_to_prereqs[prereq] # Careful thinking: getting prereqs of the prereq
                course_to_prereqs[course].update(indirect_prereqs) # UPDATE our Set
                lookup_prereq_counts[course] -= 1
                if lookup_prereq_counts[course] == 0:
                    independents.append(course)
        outputs = []
        for prereq, course in queries:
            if prereq in course_to_prereqs[course]:
                outputs.append(True)
            else:
                outputs.append(False)
        return outputs
