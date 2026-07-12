
class Solution(object):
    def deleteMiddle(self, first):
        if not first or not first.next:
            return None
        slow=first
        fast=first
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return first