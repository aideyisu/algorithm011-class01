# 迭代法
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        PreHead = ListNode(-1)
        Prev = PreHead

        while l1 and l2:
            if l1.val <= l2.val:
                Prev.next = l1
                l1 = l1.next
            else:
                Prev.next = l2
                l2 = l2.next
            Prev = Prev.next
        
        Prev.next = l1 if l1 else l2

        return PreHead.next
