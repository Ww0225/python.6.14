# 给定一个二叉树，找出其最小深度
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量
# 说明：叶子节点是指没有子节点的节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        leftMindepth = self.minDepth(root.left)
        rightMindepth = self.minDepth(root.right)
        if root.left != None and root.right == None:
            return leftMindepth+1
        if root.left == None and root.right != None:
            return rightMindepth+1
        return min(leftMindepth,rightMindepth)+1