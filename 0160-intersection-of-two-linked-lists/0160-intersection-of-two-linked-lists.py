# Definition for singly-linked list.
class ListNode(object):
    def __init__(temp, x):
        temp.val = x
        temp.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        a, b = headA, headB
        
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        
        return a
        