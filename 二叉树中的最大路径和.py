# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。
# 该路径 至少包含一个 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf

        def dfs(node:TreeNode):
            if node is None:
                return 0
            l_val = dfs(node.left)
            r_val = dfs(node.right)
            nonlocal ans
            ans = max(ans,l_val+r_val+node.val)
            return max(max(l_val,r_val)+node.val,0)

        dfs(root)
        return ans