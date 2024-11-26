# Time Complexity: O(n + m), where n is the length of `list1` and m is the length of `list2`.  
# - We traverse both linked lists once to merge them.  

# Space Complexity: O(1).  
# - We only use pointers and do not allocate extra space proportional to the input size (other than the result linked list).  

# INTUITION:  
# To merge two sorted linked lists, we can use the two-pointer approach:  
# - One pointer traverses `list1`, and the other traverses `list2`.  
# - At each step, append the smaller of the two current nodes to the merged list.  
# - Continue traversing until one of the lists is fully traversed, and then append the remaining part of the other list.  

# This approach ensures that we maintain the sorted order throughout the process, and we avoid the need for extra memory for sorting.  

# ALGORITHM:  
# 1. Create a dummy node to simplify handling the head of the merged list.  
# 2. Use a pointer (`cur`) to keep track of the current position in the merged list.  
# 3. Compare the current nodes of `list1` and `list2`:  
#    - Append the smaller node to the merged list.  
#    - Move the pointer forward in the list whose node was appended.  
# 4. When one of the lists is fully traversed, append the remaining nodes of the other list.  
# 5. Return the merged list starting from the dummy node's `next`.  

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the merging process
        dummy = ListNode()
        current = dummy

        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Append the remaining part of the non-empty list
        current.next = list1 if list1 else list2

        return dummy.next


# Example Usage:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
