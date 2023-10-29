# 给定一个二叉树 root ，返回其最大深度
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        leftHight = self.maxDepth(root.left)
        rightHight = self.maxDepth(root.right)
        return max(leftHight,rightHight)+1