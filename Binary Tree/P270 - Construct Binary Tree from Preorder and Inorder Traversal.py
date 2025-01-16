# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {}
        for i, num in enumerate(inorder):
            inorderMap[num] = i

        preOrderIndex = 0
        
        def helper(inStart, inEnd):
            nonlocal preOrderIndex
            if inStart > inEnd:
                return None

            rootVal = preorder[preOrderIndex]
            root = TreeNode(rootVal)
            preOrderIndex += 1

            mid = inorderMap[rootVal]
            root.left = helper(inStart, mid - 1)
            root.right = helper(mid + 1, inEnd)

            return root

        return helper(0, len(inorder) - 1)
        
