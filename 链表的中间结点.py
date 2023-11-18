# 给你单链表的头结点 head ，请你找出并返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow