class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class MyCircularQueue:
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.max_size = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = ListNode(value)
        if self.isEmpty():
            self.head = self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
