# Time Complexity: 
# - O(N), where N is the number of nodes in the tree
# - Each node is visited constant number of times

# Space Complexity:
# - O(1), as we only use a constant amount of extra space

# INTUITION:
# Traverse the tree level by level using next pointers, 
# creating connections between nodes at each level 
# without using additional space

# ALGO:
# 1. Start from root level
# 2. Use dummy head to track first node of next level
# 3. Connect children of nodes at current level
# 4. Move to next level using next pointers

class Solution:
   def connect(self, root: 'Node') -> 'Node':
       currentLevel = root

       while currentLevel:
           levelHead = levelPrev = Node(0)
           currentNode = currentLevel

           while currentNode:
               if currentNode.left:
                   levelPrev.next = currentNode.left
                   levelPrev = levelPrev.next

               if currentNode.right:
                   levelPrev.next = currentNode.right
                   levelPrev = levelPrev.next
               
               currentNode = currentNode.next

           currentLevel = levelHead.next

       return root
