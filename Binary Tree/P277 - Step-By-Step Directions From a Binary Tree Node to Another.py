# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - Finding LCA takes O(N) as we may need to visit all nodes
# - Building paths from LCA to start/dest nodes takes O(N) in total

# Space Complexity:
# - O(H), where H is the height of the tree
# - Space used by recursion stack for both LCA and path finding
# - Storage for path strings is O(H) as paths can't be longer than tree height

# INTUITION:
# The path between two nodes can be found by:
# 1. Finding their Lowest Common Ancestor (LCA)
# 2. Getting path from LCA to start node (all "U" moves)
# 3. Getting path from LCA to destination node (combination of "L" and "R" moves)
# 4. Combining these paths gives shortest route from start to destination

# ALGORITHM:
# 1. Find LCA of start and destination nodes using recursive search
# 2. From LCA, find paths to both nodes:
#    - For start node: count steps and convert to "U" moves
#    - For destination node: record actual "L" and "R" moves
# 3. Combine paths:
#    - First go up from start to LCA
#    - Then follow recorded path down to destination

class Solution:
   def getDirections(self, root: Optional[TreeNode], startValue: int, 
                    destValue: int) -> str:
       def findLCA(node):
           if not node or node.val == startValue or node.val == destValue:
               return node
           
           leftResult = findLCA(node.left)
           rightResult = findLCA(node.right)
           
           if leftResult and rightResult:
               return node
               
           return leftResult or rightResult
           
       def findPath(node, target, path):
           if node.val == target:
               return True
               
           if node.left and findPath(node.left, target, path):
               path += 'L'
           elif node.right and findPath(node.right, target, path):
               path += 'R'
               
           return path
       
       commonAncestor = findLCA(root)
       startPath, destPath = [], []
       
       findPath(commonAncestor, startValue, startPath)
       findPath(commonAncestor, destValue, destPath)
       
       upwardPath = 'U' * len(startPath)
       downwardPath = ''.join(destPath[::-1])
       
       return upwardPath + downwardPath
