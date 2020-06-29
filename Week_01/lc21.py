# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 迭代
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        PreHead = ListNode(-1)
        Prev = PreHead
        while l2 and l1:
            if l1.val <= l2.val:
                Prev.next = l1
                l1 = l1.next
            else:
                Prev.next = l2
                l2 = l2.next
            Prev = Prev.next
        Prev.next = l1 if l1 else l2
        return PreHead.next

# 递归
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

