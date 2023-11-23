# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。
# （即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []
        ans = []
        cur = [root]
        sign = False
        while cur:
            nxt = []
            vals = []
            for node in cur:
                vals.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            cur = nxt
            ans.append(vals[::-1] if sign else vals)
            sign = not sign
        return ans