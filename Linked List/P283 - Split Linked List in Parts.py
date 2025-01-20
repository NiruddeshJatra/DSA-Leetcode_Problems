# Time Complexity:
# - O(N), where N is the number of nodes in the linked list
# - We traverse list once to count nodes O(N)
# - Then traverse again to split into parts O(N)

# Space Complexity:
# - O(k) for the result array storing the k parts
# - We only modify existing pointers without creating new nodes
# - Space is used only for storing heads of partitions

# INTUITION:
# To split linked list into k parts as evenly as possible:
# 1. First count total nodes to know how to distribute
# 2. Calculate base length for each part and extra nodes
# 3. Create parts by:
#    - Taking base length nodes
#    - Adding one extra node if remainder exists
#    - Breaking links between parts
# 4. Fill remaining slots with null if k > number of parts

# ALGORITHM:
# 1. Count total nodes in list
# 2. Calculate:
#    - Base length = total nodes / k
#    - Remainder = total nodes % k
# 3. Create k parts:
#    - Take base length nodes
#    - Take one extra if remainder > 0
#    - Break link to next part
# 4. Fill array with null until length k

class Solution:
   def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
       # Count nodes
       nodeCount = 0
       current = head
       while current:
           nodeCount += 1
           current = current.next
           
       # Calculate partition sizes
       baseLength = nodeCount // k
       extraNodes = nodeCount % k
       if nodeCount < k:
           baseLength = 1
           extraNodes = 0
           
       # Split into parts
       result = []
       while head:
           partHead = head
           
           # Traverse to end of current part
           for i in range(baseLength - 1):
               if head:
                   head = head.next
                   
           # Add extra node if needed
           if extraNodes:
               head = head.next
               extraNodes -= 1
           
           # Break link and move to next part
           if head:
               nextPart = head.next
               head.next = None
               head = nextPart
               
           result.append(partHead)
           
       # Fill remaining parts with None
       while len(result) < k:
           result.append(None)
           
       return result
