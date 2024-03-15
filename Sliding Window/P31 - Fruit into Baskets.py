from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1) (maximum of 3 distinct fruits)

        # INTUITION:
        # This algorithm aims to find the maximum number of fruits you can collect 
        # given a list of trees, where each tree bears a type of fruit represented 
        # by an integer. You are allowed to collect fruits from at most two types 
        # of trees, but each type of tree may produce any amount of fruit. The 
        # problem is essentially asking for the length of the longest subarray 
        # containing at most two distinct elements.
        
        # ALGO:
        # 1. Initialize variables: 'ans' to store the maximum number of fruits 
        #    you can collect, 'l' as the left pointer of the sliding window, 
        #    and 'fruitCount' dictionary to count the occurrences of each type 
        #    of fruit.
        # 2. Iterate through each index 'r' in the range of the length of 'fruits'.
        #    2.1. Update the count of the current fruit type in 'fruitCount'.
        #    2.2. While the number of distinct fruit types in the current window 
        #         is greater than 2:
        #         - Decrement the count of the fruit at the left pointer 'l' 
        #           and remove it from 'fruitCount' if its count becomes zero.
        #         - Increment 'l' to move the left pointer.
        #    2.3. Update 'ans' with the maximum length of the current window.
        # 3. Return 'ans'.
        
        ans = 0
        l = 0
        fruitCount = {}
        
        for r in range(len(fruits)):
            fruitCount[fruits[r]] = 1 + fruitCount.get(fruits[r], 0)
            
            while len(fruitCount) > 2:
                fruitCount[fruits[l]] -= 1
                
                if fruitCount[fruits[l]] == 0:
                    fruitCount.pop(fruits[l])
                
                l += 1
                
            ans = max(ans, r - l + 1)
            
        return ans
