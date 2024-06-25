"""
### Problem
Given an array `asteroids` of integers representing asteroids in a row, for each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

### Intuition
When an asteroid moving to the right (`> 0`) collides with an asteroid moving to the left (`< 0`), their sizes determine the outcome. If the sizes are equal, both asteroids explode. If one is larger, it survives while the smaller one explodes. If no collision occurs (because one moves left and the other right), they both continue on their paths.

### Approach
1. **Initialize an empty stack** `ans` to keep track of asteroids that remain after collisions.
2. **Iterate through each asteroid** in the input list:
   - **Check for collisions**: While there is a potential collision (top of the stack is moving right and the current asteroid is moving left):
     - Compare the sizes of the colliding asteroids.
     - If the current asteroid is larger (in absolute value), pop the top of the stack (the right-moving asteroid).
     - If the current asteroid is smaller (in absolute value), skip adding the current asteroid to the stack.
     - If they are the same size, both explode and neither is added to the stack.
   - **No collision or stack is empty**: Add the current asteroid to the stack.
3. **Return the stack** `ans` as the final state of the asteroids.

### Algorithm
1. Initialize an empty list `ans` to represent the stack.
2. Loop through each asteroid in the input list.
3. For each asteroid, check for collisions with the asteroid at the top of the stack:
   - If they collide, compare their sizes and update the stack accordingly.
   - If no collision, or if the stack is empty, add the current asteroid to the stack.
4. Return the stack `ans`.

### Time Complexity
The time complexity is O(n), where n is the number of asteroids, as each asteroid is processed at most once.

### Space Complexity
The space complexity is O(n) for storing the resulting asteroids in the stack.

### Code
"""

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for asteroid in asteroids:
            while ans and ans[-1] > 0 and asteroid < 0:
                if ans[-1] + asteroid < 0:
                    ans.pop()  # Current asteroid is larger; pop the last one from the stack
                elif ans[-1] + asteroid > 0:
                    break  # Last asteroid in the stack is larger; current one is destroyed
                else:
                    ans.pop()  # Both asteroids are the same size; both are destroyed
                    break
            else:
                ans.append(asteroid)  # No collision or stack is empty; add current asteroid
        return ans
