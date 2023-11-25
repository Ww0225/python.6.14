# 给定一个二叉树，我们在树的节点上安装摄像头。
# 节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
# 计算监控树的所有节点所需的最小摄像头数量。
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(root:TreeNode):
            if root is None:
                return inf,0,0
            l_choose,l_by_fa,l_by_son = dfs(root.left)
            r_choose,r_by_fa,r_by_son = dfs(root.right)
            choose = min(l_choose,l_by_fa,l_by_son) + min(r_choose,r_by_fa,r_by_son) + 1
            by_fa = min(l_choose,l_by_son) + min(r_choose,r_by_son)
            by_son = min(l_choose+r_by_son,l_by_son+r_choose,l_choose+r_choose)
            return choose,by_fa,by_son

        choose, _, by_son = dfs(root)
        return min(choose, by_son)
