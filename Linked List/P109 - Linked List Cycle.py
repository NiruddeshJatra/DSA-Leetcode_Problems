# Two-Pointer Method (Floyd's Cycle-Finding Algorithm)
# Also known as the "hare and tortoise" algorithm, this method uses two pointers that traverse the list at different speeds. 
# The slow pointer moves one step at a time, while the fast pointer moves two steps. 
# If there is a cycle, the fast pointer will eventually catch up to the slow pointer.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
