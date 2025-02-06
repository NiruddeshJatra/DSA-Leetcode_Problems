# Time Complexity:
# - O(V + E) where V is number of courses and E is number of prerequisites
# - Each course is visited once
# - Each prerequisite edge is processed once
# - Building adjacency list takes O(E)

# Space Complexity:  
# - O(V + E) for adjacency list
# - O(V) for visited and path sets
# - O(V) for recursion stack
# - O(V) for result array storing topological order

# INTUITION:
# This is topological sort with cycle detection since:
# - Prerequisites form directed edges
# - Need courses in order where prerequisites come after courses that depend on them
# - If cycle exists, no valid order possible
# Example: courses=4, prereqs=[[1,0],[2,0],[3,1],[3,2]]
# Graph: 1 -> 0 <- 2
#        ↑         ↑ 
#        └── 3 ----┘
# Order: [0,1,2,3] (0 must come before 1,2 which come before 3)

# ALGO:
# 1. Build adjacency list from prerequisites
# 2. For each unvisited course:
#    - Track visited nodes and current path
#    - DFS through prerequisites
#    - If cycle found, return empty list (impossible)
#    - Add course to result after visiting all prerequisites
# 3. Return courses in topological order

class Solution:
   def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
       def hasCycle(currentCourse: int) -> bool:
           """
           DFS to detect cycles and build topological order.
           Returns True if cycle found, False otherwise.
           """
           visitedCourses.add(currentCourse)
           currentPath.add(currentCourse)
           
           # Check all prerequisites
           for prereq in adjacencyList[currentCourse]:
               if prereq not in visitedCourses:
                   if hasCycle(prereq):
                       return True
               # Cycle found if prereq in current path
               elif prereq in currentPath:
                   return True
           
           # No cycle found, add to result
           currentPath.remove(currentCourse)
           courseOrder.append(currentCourse)
           return False
       
       # Initialize data structures
       visitedCourses = set()
       currentPath = set()
       adjacencyList = defaultdict(set)
       courseOrder = []
       
       # Build prerequisite graph
       for course, prereq in prerequisites:
           adjacencyList[course].add(prereq)
           
       # Process all courses
       for course in range(numCourses):
           if course not in visitedCourses:
               if hasCycle(course):
                   return []  # Cycle found, no valid order
                   
       return courseOrder
