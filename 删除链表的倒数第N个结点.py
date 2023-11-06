#给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=fast=dummy=ListNode(next=head)
        for _ in range(n):
            fast=fast.next
        while fast and fast.next:
            slow,fast=slow.next,fast.next
        slow.next=slow.next.next
        return dummy.next