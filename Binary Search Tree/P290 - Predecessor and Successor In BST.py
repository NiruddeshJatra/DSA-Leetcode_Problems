# Time Complexity:
# - O(N) where N is the number of nodes in the binary tree
# - We perform a complete inorder traversal of the tree

# Space Complexity:
# - O(H) where H is the height of the tree, for recursion stack
# - In worst case (skewed tree), it could be O(N)
# - In balanced tree, it would be O(log N)

# INTUITION:
# Using inorder traversal of BST gives nodes in sorted order. 
# For any value K:
# - Its predecessor is the largest value smaller than K
# - Its successor is the smallest value larger than K
# By tracking these conditions during inorder traversal, we can find both in a single pass.

# ALGO:
# 1. Initialize predecessor and successor as -1
# 2. Perform inorder traversal:
#    - If current node value > key and no successor found yet:
#      Update successor (first larger value)
#    - If current node value < key:
#      Update predecessor (largest smaller value so far)
# 3. Return predecessor and successor pair

from os import *
from sys import *
from collections import *
from math import *

class BinaryTreeNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

def findPreSuc(root: BinaryTreeNode, targetKey: int) -> List[int]:
   predecessor = successor = -1
   
   def inorderTraversal(currentNode: BinaryTreeNode) -> None:
       nonlocal predecessor, successor
       
       if not currentNode:
           return
           
       # Left subtree
       inorderTraversal(currentNode.left)
       
       # Process current node
       if targetKey < currentNode.data:
           if successor == -1:  # First larger value found
               successor = currentNode.data
       elif targetKey > currentNode.data:
           predecessor = currentNode.data  # Keep updating to get largest smaller value
           
       # Right subtree
       inorderTraversal(currentNode.right)
   
   inorderTraversal(root)
   return [predecessor, successor]
