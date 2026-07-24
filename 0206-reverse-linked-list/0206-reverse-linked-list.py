
class Solution(object):
    def reverseList(self, head):
       prev=None
       cur=head
       while cur:
          next=cur.next
          cur.next=prev
          prev=cur
          cur=next
       return prev
        