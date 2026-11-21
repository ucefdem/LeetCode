class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
## 1st version
        
# def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
#         if l1.next != None or l2.next != None: 
#             if l1.next == None: l1.next = ListNode(0,None)
#             if l2.next == None: l2.next = ListNode(0,None)
#             if (l1.val + l2.val) >= 10 : l1.next.val += 1
#             return ListNode((l1.val + l2.val) % 10, next=self.addTwoNumbers(l1.next, l2.next))
#         if (l1.val + l2.val) >= 10 :
#             return ListNode((l1.val + l2.val) % 10, ListNode(1, None))
#         return ListNode((l1.val + l2.val) % 10)


def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry = 0
        out = ListNode()
        curr = out
        while l1 or l2 or carry:
            if l1 == None: l1 = ListNode(0, None)
            if l2 == None: l2 = ListNode(0, None)
            total = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            curr.next = ListNode(total, None)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        return out.next

