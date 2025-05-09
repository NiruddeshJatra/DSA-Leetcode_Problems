# Time Complexity:
# - O(k^n), where k is the number of children and n is the number of cookie bags
# - We explore k choices for each cookie bag
# - Optimization techniques like sorted input and pruning improve real-world performance

# Space Complexity:
# - O(k + n), where k is the number of children and n is the number of cookie bags
# - O(k) for the children array to track cookies per child
# - O(n) for the recursion stack depth in the worst case

# INTUITION:
# The problem asks for the minimized unfairness when distributing cookies to k children
# Unfairness is defined as the maximum number of cookies any child gets
# Key strategy:
# - Use backtracking to try all possible distributions
# - Apply optimization techniques to prune the search space
# Example:
# cookies = [8,15,10,20,8], k = 2
# One optimal distribution: [8,15,8] and [10,20]
# Child 1 gets 31 cookies, Child 2 gets 30 cookies
# Maximum is 31, which is the minimal unfairness possible

# ALGO:
# 1. Sort cookie bags in descending order for better pruning
# 2. Use backtracking to assign each cookie bag to a child
# 3. Apply multiple pruning techniques:
#    - Skip assignments that would exceed our current best answer
#    - Break early when current child has received 0 cookies
#      (symmetric distributions)
# 4. Track the minimum maximum cookies per child (unfairness)

class Solution:
   def distributeCookies(self, cookies: List[int], k: int) -> int:
       # Initialize tracking array for cookies assigned to each child
       childrenCookies = [0] * k
       
       # Sort cookie bags in descending order for better pruning
       cookies.sort(reverse=True)
       
       # Initialize answer with a large value
       minUnfairness = float('inf')
       
       def backtrack(cookieIndex):
           nonlocal minUnfairness
           
           # Base case: all cookies have been distributed
           if cookieIndex == len(cookies):
               # Calculate unfairness as maximum cookies any child has
               return max(childrenCookies)
           
           # Try assigning current cookie bag to each child
           for childIndex in range(k):
               # Pruning: Skip if this assignment would exceed our current best answer
               if childrenCookies[childIndex] + cookies[cookieIndex] >= minUnfairness:
                   continue
               
               # Assign cookie bag to this child
               childrenCookies[childIndex] += cookies[cookieIndex]
               
               # Recursively assign remaining cookie bags
               currentUnfairness = backtrack(cookieIndex + 1)
               minUnfairness = min(minUnfairness, currentUnfairness)
               
               # Backtrack: remove cookie bag from this child
               childrenCookies[childIndex] -= cookies[cookieIndex]
               
               # Pruning: If this child has no cookies, break
               # This avoids symmetric distributions (child1=a,child2=b is same as child1=b,child2=a)
               if childrenCookies[childIndex] == 0:
                   break
           
           return minUnfairness
       
       # Start backtracking from the first cookie bag
       return backtrack(0)
