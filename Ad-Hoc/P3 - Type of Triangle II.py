# Time Complexity: O(1)
# Space Complexity: O(1)


def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        elif nums[0]==nums[1] and nums[0]==nums[2]:
            return "equilateral"
        elif nums[0]==nums[1] or nums[1]==nums[2] or nums[2]==nums[0]:
            return "isosceles"
        else:
            return "scalene"
