# 给你二叉树的根节点root和一个表示目标和的整数targetSum
# 判断该树中是否存在根节点到叶子节点的路径,这条路径上所有节点值相加等于目标和targetSum.
# 如果存在，返回 true ；否则，返回 false
# 叶子节点 是指没有子节点的节点
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)