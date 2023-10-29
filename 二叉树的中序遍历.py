#给定一个二叉树的根节点 root ，返回它的中序遍历
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 法一：递归实现
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root == 'null':
            return
        res = []
        self.inorder(root,res)
        return res
    def inorder(self,node:TreeNode,res:list[int])->None:
        if not node:
            return
        self.inorder(node.left,res)
        res.append(node.val)
        self.inorder(node.right,res)
    #法二：莫里斯遍历
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res, stack = list(), list()
        curr = root
        while curr or len(stack):
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            res.append(node.val)
            curr = node.right
        return res