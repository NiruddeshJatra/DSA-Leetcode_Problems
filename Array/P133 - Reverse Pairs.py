# Time Complexity: O(n log n), where n is the number of elements in the array.
# This is because the merge sort algorithm, which forms the basis of this approach, runs in O(n log n) time.

# Space Complexity: O(n), because of the extra space required for the temporary arrays used during the merge process.

# INTUITION:
# A reverse pair in an array is defined as a pair of indices (i, j) such that i < j and nums[i] > 2 * nums[j].
# The idea is to use a modified merge sort to count reverse pairs efficiently. During the merge step, 
# we count the reverse pairs between the left and right halves before merging them together.

# ALGO:
# 1. Recursively divide the array into two halves using merge sort.
# 2. While merging two halves, count the reverse pairs such that nums[i] > 2 * nums[j] where i is in the left half and j is in the right half.
# 3. After counting the reverse pairs, merge the two sorted halves.
# 4. Return the total number of reverse pairs.

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(start, end):
            # Base case: If the array has one or no elements, there are no reverse pairs
            if start >= end:
                return 0

            # Divide the array into two halves
            mid = (start + end) // 2

            # Recursively count reverse pairs in the left and right halves
            cnt = mergeSort(start, mid) + mergeSort(mid + 1, end)

            # Count reverse pairs where nums[l] > 2 * nums[r]
            l, r = start, mid + 1
            while l <= mid and r <= end:
                if nums[l] > 2 * nums[r]:
                    cnt += mid - l + 1
                    r += 1
                else:
                    l += 1

            # Merge the two sorted halves
            nums[start:end + 1] = sorted(nums[start:end + 1])

            # Return the total count of reverse pairs
            return cnt

        # Start the merge sort process from the entire array
        return mergeSort(0, len(nums) - 1)
