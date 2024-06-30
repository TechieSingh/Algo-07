class Solution:
    def sum(self, a: int, b: int) -> int:
        alist = Slist(a)
        blist = Slist(b)
        clist = Slist()
        work = [0] # work done by alg
        show = False
        s = Exam(alist,blist,clist,work,show)
        ans = clist.Int()
        return ans

############################################################
# Exam.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2024
###########################################################

############################################################
#  ADD HERE
###########################################################

############################################################
#  ListNode class
#  NOTHING CAN BE CHANGED IN THIS CLASS
###########################################################
class ListNode:
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next

    def change_value(self,x:'int')->'None':
        self.val = x

############################################################
#  Slist class
#  WRITE CODE ONLY IN SLIST CLASS
###########################################################
class Slist:
    def __init__(self, n: 'Python Int' = None):
        self._first = None
        self._last = None
        self._is_positive = True
        
        # List from the number 
        # Handles negative numbers 
        if n is not None:
            if n < 0:
                self._is_positive = False
                n = -n

            for d in str(n):
                new_node = ListNode(int(d))
                if self._first is None:
                    self._first = new_node
                    self._last = new_node
                else:
                    self._last.next = new_node
                    self._last = new_node
        
        

    ######################################################
    # This routine is only for testing. You cannot use it
    # You cannot convert slist to PYTHON INT or any other data structure
    ####################################################
    def Int(self)->'python int':
        s = 0
        sign = self.is_positive()
        n = self._first 
        assert(n)
        l = len(self)
        if (l > 1):
          if (n.val == 0):
            print(self)
            print("You cannot have leading zero")
            assert(0)
        if (l == 1 and n.val == 0):
            if (sign == False):
                print(self)
                print("There is no -0")
                assert(0)
        
        while (n != None):
          v = n.val 
          if (v < 0 or v > 9):
            print(self)
            print("YOU MUST STORE SINGLE DIGIT 0 to 9 only with each node")
            assert(0)
          s = (10 * s)  + v
          n = n.next
        if (sign == False):
          s = -s
        return s
       
        
    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################

    #############################
    # YOU MUST WRITE whether the number represented in Slist + or -
    # NOTE THERE IS NO -0. For 0 sign must be positive
    #############################
    def is_positive(self) -> 'Bool':
        return self._is_positive

    def is_negative(self) -> 'Bool':
        return not self._is_positive

    def __len__(self) -> 'int':
        count = 0
        cur = self._first
        while cur:
            count += 1
            cur = cur.next
        return count

    def __str__(self) -> str:
        nodes = []
        current = self._first

        if self.is_negative():
            nodes.append("-")

        while current:
            nodes.append(str(current.val))
            current = current.next

        nodes.append("None")
        return "->".join(nodes)

    
def add_two_numbers(l1: 'ListNode', l2: 'ListNode', work: 'list') -> 'ListNode':
    # Adds two numbers using stacks, without reverse lists twice
    dummy = ListNode(0)
    cur = dummy
    carry = 0

    stack1 = []
    stack2 = []

    while l1:
        stack1.append(l1.val)
        l1 = l1.next

    while l2:
        stack2.append(l2.val)
        l2 = l2.next

    while stack1 or stack2 or carry:
        x = stack1.pop() if stack1 else 0
        y = stack2.pop() if stack2 else 0
        total = carry + x + y
        carry = total // 10
        cur.next = ListNode(total % 10)
        cur = cur.next
        work[0] += 1

    return reverse_list(dummy.next)


def reverse_list(head: 'ListNode') -> 'ListNode':
    # Reverses a linked list
    prev = None
    curr = head
    while curr is not None:
        next_tmp = curr.next
        curr.next = prev
        prev = curr
        curr = next_tmp
    return prev

########################################
# Calling code
########################################
class Exam:
    def __init__(self, a: 'Slist', b: 'Slist', clist: 'Empty Slist', work: 'list of size 1 that has int', show: 'Bool') -> 'None':
        if show:
            print("a =", a)
            print("b =", b)

        apos = a.is_positive()
        bpos = b.is_positive()

        if not apos and not bpos:
            sum_list = add_two_numbers(a._first, b._first, work)
            clist._first = sum_list
            clist._is_positive = False
        elif apos and bpos:
            sum_list = add_two_numbers(a._first, b._first, work)
            clist._first = sum_list
            clist._is_positive = True
        else:
            if self.compare_abs(a, b) >= 0:
                diff_list = self.subtract_lists(a._first, b._first, work)
                clist._first = diff_list
                clist._is_positive = apos
            else:
                diff_list = self.subtract_lists(b._first, a._first, work)
                clist._first = diff_list
                clist._is_positive = bpos

        # Ensure there is no -0 and remove leading zeros
        if clist._first is not None and clist._first.val == 0:
            clist._is_positive = True

        if show:
            print("a + b =", clist)
            print("work =", work[0])

    def compare_abs(self, a: 'Slist', b: 'Slist') -> int:
        lena, lenb = len(a), len(b)
        if lena != lenb:
            return lena - lenb

        curra, currb = a._first, b._first
        while curra and currb:
            if curra.val != currb.val:
                return curra.val - currb.val
            curra = curra.next
            currb = currb.next
        return 0

    def subtract_lists(self, l1: 'ListNode', l2: 'ListNode', work: 'list') -> 'ListNode':
        stack1 = []
        stack2 = []
        # Subtracts two numbers using stacks
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while stack1 or stack2:
            x = stack1.pop() if stack1 else 0
            y = stack2.pop() if stack2 else 0
            diff = x - y + carry
            if diff < 0:
                carry = -1
                diff += 10
            else:
                carry = 0
            curr.next = ListNode(diff)
            curr = curr.next
            work[0] += 1

        result = reverse_list(dummy.next)
        while result is not None and result.val == 0:
            result = result.next

        return result if result is not None else ListNode(0)




