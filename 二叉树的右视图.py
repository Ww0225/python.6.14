# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        ans = []

        def f(node,depth):
            if node is None:
                return
            if len(ans) == depth:
                ans.append(node.val)
            f(node.right,depth+1)
            f(node.left,depth+1)

        f(root,0)
        return ans