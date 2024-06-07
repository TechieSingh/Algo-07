class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Slist:
    def __init__(self):
        self._first = None
        self._last = None
        self._len = 0

    def push(self, val):
        new_node = ListNode(val, self._first)
        self._first = new_node
        if self._len == 0:
            self._last = new_node
        self._len += 1

    def pop(self):
        if self._len == 0:
            raise IndexError("pop from empty list")
        val = self._first.val
        self._first = self._first.next
        self._len -= 1
        if self._len == 0:
            self._last = None
        return val

    def peek(self):
        if self._len == 0:
            raise IndexError("peek from empty list")
        return self._first.val

    def is_empty(self):
        return self._len == 0

    def __len__(self):
        return self._len


class MyStack:
    def __init__(self):
        self._s = Slist()

    def push(self, x: int) -> None:
        self._s.push(x)

    def pop(self) -> int:
        return self._s.pop()

    def top(self) -> int:
        return self._s.peek()

    def empty(self) -> bool:
        return self._s.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
