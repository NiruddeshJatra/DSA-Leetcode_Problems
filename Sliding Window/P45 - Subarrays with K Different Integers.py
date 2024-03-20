# Time Complexity: O(n)
# Space Complexity: O(n)

# INTUITION:
# The function 'helper' calculates the number of subarrays in the array 'arr' having at most 'k' distinct elements.
# It uses a sliding window approach with a dictionary 'count' to keep track of the count of each distinct element 
# within the current window. The function iterates through the array and maintains the sliding window such that 
# the number of distinct elements within the window is at most 'k', updating the count of subarrays accordingly.

# ALGORITHM:
# 1. Define a helper function 'helper' to calculate the number of subarrays with at most 'k' distinct elements:
#    1.1 Initialize a left pointer 'l' and the answer 'ans' to 0.
#    1.2 Initialize an empty dictionary 'count' to store the count of distinct elements.
#    1.3 Iterate through the array 'arr' using the right pointer 'r':
#        1.3.1 Increment the count of 'arr[r]' in the 'count' dictionary.
#        1.3.2 While the number of distinct elements in the 'count' dictionary is greater than 'k':
#              1.3.2.1 Decrement the count of 'arr[l]' in the 'count' dictionary.
#              1.3.2.2 If the count of 'arr[l]' becomes 0, remove it from the 'count' dictionary.
#              1.3.2.3 Increment 'l'.
#        1.3.3 Update 'ans' by adding the length of the subarray from 'l' to 'r'.
#    1.4 Return 'ans'.
# 2. Define the function 'kDistinctSubarrays' which calculates the number of subarrays in 'arr' with exactly 'k' distinct elements:
#    2.1 Return the difference between the results of calling 'helper' with arguments 'arr', 'n', and 'k', and calling 'helper' with arguments 'arr', 'n', and 'k - 1'.

def helper(arr, n, k):
    l, ans = 0, 0
    count = {}
    for r in range(n):
        count[arr[r]] = 1 + count.get(arr[r], 0)
        while len(count) > k:
            count[arr[l]] -= 1
            if count[arr[l]] == 0:
                count.pop(arr[l])
            l += 1
        ans += (r - l + 1)
    return ans

def kDistinctSubarrays(arr, n, k):
    return helper(arr, n, k) - helper(arr, n, k - 1)
