# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。
# 如果两个链表不存在相交节点，返回 null 。
# 图示两个链表在节点 c1 开始相交：
# 题目数据 保证 整个链式结构中不存在环。
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        B = headB
        while A!=B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A