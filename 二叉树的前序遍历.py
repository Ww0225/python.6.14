# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preOrder(self,root:TreeNode,res):
        if not root:
            return
        res.append(root.val)
        self.preOrder(root.left,res)
        self.preOrder(root.right,res)

    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        self.preOrder(root,res)
        return res