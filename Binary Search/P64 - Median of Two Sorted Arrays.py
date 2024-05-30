# Time Complexity: O(m + n)
# Space Complexity: O(m + n)

# INTUITION:
# To find the median of two sorted arrays, we need to merge them into a single sorted array and then find the median of the resulting array. The merged array will have a length equal to the sum of the lengths of the two input arrays. The median can then be found based on whether the merged array has an odd or even number of elements.

# ALGO:
# 1. Initialize two indices, `index1` and `index2`, to traverse through `nums1` and `nums2` respectively.
# 2. Create an empty list `temp` to store the merged elements.
# 3. Traverse both arrays and compare the current elements:
#    - Append the smaller element to `temp` and move the corresponding index.
# 4. If there are remaining elements in `nums1`, append them to `temp`.
# 5. If there are remaining elements in `nums2`, append them to `temp`.
# 6. Calculate the middle index `mid` of the merged array `temp`.
# 7. If the length of `temp` is even, return the average of the two middle elements.
# 8. If the length of `temp` is odd, return the middle element.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index1, index2 = 0, 0
        temp = []

        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] < nums2[index2]:
                temp.append(nums1[index1])
                index1 += 1
            else:
                temp.append(nums2[index2])
                index2 += 1

        if index1 < len(nums1):
            temp.extend(nums1[index1 : len(nums1)])

        if index2 <= len(nums2):
            temp.extend(nums2[index2 : len(nums2)])

        mid = len(temp)//2
        if len(temp)%2 == 0:
            return (temp[mid]+temp[mid-1])/2
        else:
            return temp[mid]
