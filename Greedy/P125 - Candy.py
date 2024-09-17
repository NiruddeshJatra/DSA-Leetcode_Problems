# Time Complexity: O(n), where n is the number of children. The two passes through the `ratings` list (left to right and right to left) both take linear time.
# Space Complexity: O(n), as we are using an extra array `candies` to store the number of candies assigned to each child.

# INTUITION:
# The idea is to ensure that each child receives at least one candy and that children with higher ratings than their neighbors get more candies. We can achieve this by making two passes over the `ratings` array:
# 1. A forward pass to ensure each child has more candies than their left neighbor if their rating is higher.
# 2. A backward pass to ensure each child has more candies than their right neighbor if their rating is higher.

# ALGO:
# 1. Initialize an array `candies` of size equal to `ratings` with all values set to 1, since each child must receive at least 1 candy.
# 2. Perform a forward pass through the `ratings`:
#    2.1 For each child from left to right (starting from the second child), if the current child has a higher rating than the previous child and does not have more candies, increment the current child’s candies to be one more than the previous child.
# 3. Perform a backward pass through the `ratings`:
#    3.1 For each child from right to left (starting from the second-last child), if the current child has a higher rating than the next child and does not have more candies, increment the current child’s candies to be one more than the next child.
# 4. Sum all the values in the `candies` array to get the total number of candies required.

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Step 1: Initialize candies array with 1 candy for each child
        candies = [1] * len(ratings)
        
        # Step 2: Forward pass to ensure each child has more candies than their left neighbor if rating is higher
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                candies[i] = candies[i-1] + 1
        
        # Step 3: Backward pass to ensure each child has more candies than their right neighbor if rating is higher
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1
        
        # Step 4: Return the total number of candies required
        return sum(candies)
