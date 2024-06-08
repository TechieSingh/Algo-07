class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Slist:
    def __init__(self):
        self._first = None
        self._last = None
        self._len = 0

class MyCircularQueue:
    def __init__(self, k: int):
        self._capacity = k
        self._size = 0
        self._head = None
        self._tail = None

    def enQueue(self, value: int) -> bool:
        if self._size == self._capacity:
            return False
        new_node = ListNode(value)
        if self._size == 0:
            self._head = self._tail = new_node
            self._tail.next = self._head
        else:
            self._tail.next = new_node
            self._tail = new_node
            self._tail.next = self._head
        self._size += 1
        return True

    def deQueue(self) -> bool:
        if self._size == 0:
            return False
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._tail.next = self._head
        self._size -= 1
        return True

    def Front(self) -> int:
        if self._size == 0:
            return -1
        return self._head.val

    def Rear(self) -> int:
        if self._size == 0:
            return -1
        return self._tail.val

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size == self._capacity





