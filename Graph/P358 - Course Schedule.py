# Time Complexity:
# - O(V + E) where V is number of courses and E is number of prerequisites
# - We process each vertex once through the queue
# - For each vertex, we process its outgoing edges once
# - Each edge is processed exactly once when reducing indegrees

# Space Complexity:
# - O(V) for indegrees array and queue in worst case
# - O(E) for adjacency list representation
# - Overall space: O(V + E)

# INTUITION:
# Imagine planning your college courses. Some courses have prerequisites:
# - You need Calculus 1 before Calculus 2
# - You need Physics 1 before Physics 2
# - You need Programming before Data Structures
#
# To determine if you can graduate:
# 1. Find courses with no prerequisites - you can take these first
# 2. After completing these, what new courses are now available?
# 3. Continue this process until either:
#    - You can take all courses (success!)
#    - You're stuck with remaining courses but can't take any (cycle detected)
#
# This is exactly what Kahn's algorithm does with indegrees:
# - indegree = number of prerequisites for each course
# - When indegree becomes 0, you can take that course

# ALGORITHM:
# 1. Build adjacency list and count prerequisites (indegrees) for each course
# 2. Find all courses with no prerequisites (indegree = 0)
# 3. For each course we can take:
#    - Process its dependent courses (reduce their indegrees)
#    - When a course's indegree becomes 0, we can take it next
# 4. If we can take all courses (queue length = numCourses), no cycles exist

class Solution:
   def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       # Track number of prerequisites for each course
       prerequisiteCount = [0] * numCourses
       # Build adjacency list: course -> list of dependent courses
       courseDependencies = defaultdict(set)
       
       # Process prerequisites to build graph
       for dependentCourse, prerequisiteCourse in prerequisites:
           courseDependencies[prerequisiteCourse].add(dependentCourse)
           prerequisiteCount[dependentCourse] += 1
       
       # Find all courses that can be taken immediately (no prerequisites)
       availableCourses = []
       for course in range(numCourses):
           if prerequisiteCount[course] == 0:
               availableCourses.append(course)
       
       # Process each available course
       for completedCourse in availableCourses:
           # After completing this course, update dependent courses
           for dependentCourse in courseDependencies[completedCourse]:
               prerequisiteCount[dependentCourse] -= 1
               # If all prerequisites met, course becomes available
               if prerequisiteCount[dependentCourse] == 0:
                   availableCourses.append(dependentCourse)
       
       # If we can take all courses, no cycles exist
       return len(availableCourses) == numCourses
