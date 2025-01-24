# Time Complexity: O(candies)
# Space Complexity: O(n)

# INTUITION:
# Distribute candies cyclically to n people, incrementing distribution amount each round
# Ensure equal/fair distribution while respecting total candy count

class Solution:
   def distributeCandies(self, candies: int, n: int) -> List[int]:
       distribution = [0] * n
       person, candyAmount = 0, 1

       while candies:
           if person == n:
               person = 0
           
           giveAmount = min(candyAmount, candies)
           distribution[person] += giveAmount
           candies -= giveAmount
           
           candyAmount += 1
           person += 1

       return distribution
