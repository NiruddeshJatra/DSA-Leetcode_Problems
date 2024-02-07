class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = 0
        sum = 0
        for i in nums:
            sum += i
            if sum==0:
                ans+=1
        return ans
