# Course Schedule (can all courses be taken?)
# Input: n courses, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Read [a, b] as "b must be taken before a" (b -> a)
from collections import defaultdict, deque


def course_schedule(n_courses, prerequisites):
    in_degree = [0] * n_courses
    graph = defaultdict(list)

    for course, prereqs in prerequisites:
        graph[prereqs].append(course)   # prerequisite → course
        in_degree[course] += 1

    queue = deque(i for i in range(n_courses) if in_degree[i] == 0)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return len(result) == n_courses


print(course_schedule(4, [[1,0],[2,0],[3,1],[3,2]]))