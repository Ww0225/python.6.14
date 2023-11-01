# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）
class MyStack:
    #法一：单队列
    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)
        q_length = len(self.q)
        while q_length > 1:
            self.q.append(self.q.pop(0))
            q_length -= 1

    def pop(self) -> int:
        return self.q.pop(0)

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not bool(self.q)

    #法二：双队列