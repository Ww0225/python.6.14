# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
# 完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，
# 其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。
# 若最底层为第 h 层，则该层包含 1~ 2h 个节点
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def height(self,root:TreeNode)->int:
        height = 0
        while root:
            root = root.left
            height+=1
        return height
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        if leftHeight == rightHeight:
            return (2**leftHeight-1)+self.countNodes(root.right)+1
        else:
            return (2**rightHeight-1)+self.countNodes(root.left)+1
