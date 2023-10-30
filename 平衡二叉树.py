# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left)-self.depth(root.right)) <= 1 \
            and self.isBalanced(root.left) and self.isBalanced(root.right)
    def depth(self,root):
        if not root:
            return 0
        return max(self.depth(root.left),self.depth(root.right))+1
