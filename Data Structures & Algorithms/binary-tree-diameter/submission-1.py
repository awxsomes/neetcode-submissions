# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        def dfs(root):
            nonlocal maxi
            if root == None:
                return 0
            right =dfs(root.right)
            left= dfs(root.left)
            maxi= max(maxi, right+left)
            return max(left,right)+1
        dfs(root)
        return maxi
        