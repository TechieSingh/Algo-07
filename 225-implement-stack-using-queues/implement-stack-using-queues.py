class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Slist:
    def __init__(self):
        self._first = None
        self._last = None
        self._len = 0

class MyStack:
    def __init__(self):
        self._s = Slist()

    def push(self, x: int) -> None:
        new_node = ListNode(x, self._s._first)
        self._s._first = new_node
        if self._s._len == 0:
            self._s._last = new_node
        self._s._len += 1

    def pop(self) -> int:
        if self._s._len == 0:
            raise IndexError("pop from empty stack")
        val = self._s._first.val
        self._s._first = self._s._first.next
        self._s._len -= 1
        if self._s._len == 0:
            self._s._last = None
        return val

    def top(self) -> int:
        if self._s._len == 0:
            raise IndexError("top from empty stack")
        return self._s._first.val

    def empty(self) -> bool:
        return self._s._len == 0

