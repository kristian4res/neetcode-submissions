# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node acts as the anchor for the head of our new list
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        # Continue if there are digits left in l1, l2, or a remaining carry
        while l1 or l2 or carry:
            # Extract digits, default to 0 if the list has ended
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Compute sum for this position
            total = v1 + v2 + carry
            carry = total // 10            # 1 if total >= 10, else 0
            cur.next = ListNode(total % 10) # Store the single digit

            # Move current pointer forward
            cur = cur.next

            # Advance input lists if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the actual head of the resulting list
        return dummy.next
