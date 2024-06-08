class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Slist:
    def __init__(self):
        self._first = None
        self._last = None
        self._len = 0

class MyQueue:
    def __init__(self):
        self._in_stack = Slist()
        self._out_stack = Slist()

    def _transfer(self) -> None:
        while self._in_stack._len > 0:
            node = self._in_stack._first
            self._in_stack._first = self._in_stack._first.next
            node.next = self._out_stack._first
            self._out_stack._first = node
            self._in_stack._len -= 1
            self._out_stack._len += 1

    def push(self, x: int) -> None:
        new_node = ListNode(x)
        new_node.next = self._in_stack._first
        self._in_stack._first = new_node
        self._in_stack._len += 1

    def pop(self) -> int:
        if self._out_stack._len == 0:
            self._transfer()
        if self._out_stack._len == 0:
            raise IndexError("pop from empty queue")
        val = self._out_stack._first.val
        self._out_stack._first = self._out_stack._first.next
        self._out_stack._len -= 1
        return val

    def peek(self) -> int:
        if self._out_stack._len == 0:
            self._transfer()
        if self._out_stack._len == 0:
            raise IndexError("peek from empty queue")
        return self._out_stack._first.val

    def empty(self) -> bool:
        return self._in_stack._len == 0 and self._out_stack._len == 0


