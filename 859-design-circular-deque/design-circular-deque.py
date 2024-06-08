class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Slist:
    def __init__(self):
        self._first = None
        self._last = None
        self._len = 0


class MyCircularDeque:
    def __init__(self, k: int):
        self._capacity = k
        self._size = 0
        self._head = None
        self._tail = None

    def insertFront(self, value: int) -> bool:
        if self._size == self._capacity:
            return False
        new_node = ListNode(value)
        if self._size == 0:
            self._head = self._tail = new_node
            self._tail.next = self._head
        else:
            new_node.next = self._head
            self._head = new_node
            self._tail.next = self._head
        self._size += 1
        return True

    def insertLast(self, value: int) -> bool:
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

    def deleteFront(self) -> bool:
        if self._size == 0:
            return False
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._tail.next = self._head
        self._size -= 1
        return True

    def deleteLast(self) -> bool:
        if self._size == 0:
            return False
        if self._size == 1:
            self._head = self._tail = None
        else:
            current = self._head
            while current.next != self._tail:
                current = current.next
            current.next = self._head
            self._tail = current
        self._size -= 1
        return True

    def getFront(self) -> int:
        if self._size == 0:
            return -1
        return self._head.val

    def getRear(self) -> int:
        if self._size == 0:
            return -1
        return self._tail.val

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size == self._capacity

