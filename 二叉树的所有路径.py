# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
# 叶子节点 是指没有子节点的节点
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getPaths(self,root,path,res):
        if not root:
            return
        path += str(root.val)
        if not root.left and not root.right:
            res.append(path)
        else:
            path += '->'
            self.getPaths(root.left,path,res)
            self.getPaths(root.right,path,res)
                
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        res = []
        self.getPaths(root,'',res)
        return res