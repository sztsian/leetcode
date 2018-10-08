#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ps = ListNode(-1)
        p1 = l1
        p2 = l2
        while(p2.next):
            print("l1--", end='')
            printlist(l1)
            print("p1--", end='')
            printlist(p1)
            print("p2--", end='')
            printlist(p2)
            if p1.val >= p2.val:
                ps = ListNode(p2.val)
                ps.next = p1
                l1 = ps
                p2 = p2.next
            else:
                p1 = p1.next


def printlist(pl):
    ptest = pl
    while (ptest.next):
        print(ptest.val, end='')
        print(", ", end='')
        ptest = ptest.next
    print()

if __name__ == "__main__":
    head1 = ListNode(-1)
    head2 = ListNode(-1)
    p2 = ListNode(0)
    for i in [4, 2, 1]:
        p = head1
        head1 = ListNode(i)
        head1.next = p
    for i in [4, 3, 1]:
        p = head2
        head2 = ListNode(i)
        head2.next = p
    s1 = Solution().mergeTwoLists
    printlist(s1(head1, head2))
