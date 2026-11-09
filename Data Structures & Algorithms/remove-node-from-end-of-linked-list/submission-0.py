# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Create a dummy node pointing to the head
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # 2. Advance `right` pointer n steps ahead
        while n > 0:
            right = right.next
            n -= 1

        # 3. Move both pointers until `right` reaches the end (None)
        while right:
            left = left.next
            right = right.next

        # 4. Skip the target node
        left.next = left.next.next

        # 5. Return the new head (dummy.next handles the case where original head is deleted)
        return dummy.next