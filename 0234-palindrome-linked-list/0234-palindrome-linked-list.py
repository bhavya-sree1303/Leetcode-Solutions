class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True