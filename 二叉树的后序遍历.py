from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorder(self,root:TreeNode,res):
        if not root:
            return
        self.postorder(root.left,res)
        self.postorder(root.right,res)
        res.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        self.postorder(root,res)
        return res