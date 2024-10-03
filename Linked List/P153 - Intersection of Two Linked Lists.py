# Time Complexity: O(m + n), where m and n are the lengths of the two linked lists. 
# The algorithm traverses each list once.

# Space Complexity: O(1), since only a constant amount of extra space is used for pointers.

# INTUITION:
# The problem is to find the node at which two linked lists intersect. 
# If the two linked lists have different lengths, we can align their starting points by switching 
# the traversal paths after reaching the end of a list. This allows both pointers to traverse 
# the same number of nodes in the second traversal and meet at the intersection point.

# ALGO:
# 1. Initialize two pointers, one for each linked list.
# 2. Traverse both lists until the pointers meet. 
#    - If a pointer reaches the end of a list, switch it to the head of the other list.
#    - This ensures that both pointers traverse an equal number of nodes when they meet.
# 3. If the lists intersect, the pointers will meet at the intersection node. 
#    If not, both will reach the end (`None`).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Initialize two pointers to traverse each list
        pA, pB = headA, headB
        
        # Traverse both lists. When a pointer reaches the end of a list, switch it to the head of the other list.
        while pA != pB:
            pA = pA.next if pA else headB  # If pA reaches the end of list A, switch to headB
            pB = pB.next if pB else headA  # If pB reaches the end of list B, switch to headA
        
        # Return the intersection node or None if there's no intersection
        return pA
