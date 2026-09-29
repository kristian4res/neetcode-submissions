# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow pointers
        # reorder pattern: order list by taking a value from each side, beginnning and end, then alternate, e.g. 1, 2, 3, 4 => 1, 4, 2, 3
        # 1) split in half using fast and slow pointers - fast pointer will reach the end twice as fast as slow, so when fast hits the end, slow will be near the mid. this works for both even and odd lengths 
        # 2) first half remains the same, and the second half will be reversed to make merging easier, e.g. [1, 2] and [4, 3]
        # 3) merge two halves and the last node will now point to null, e.g. [1, 2] and [4, 3] => [1, 4, 2, 3]

        # 1) Traverse and split into halves
        slow, fast = head, head.next;
        while fast and fast.next:
            slow = slow.next;
            fast = fast.next.next;

        # 2) Define 1st and 2nd halves
        second = slow.next;
        slow.next = None;
        prev = None;
        # Reverse 2nd half to make merging easier
        while second:
            tmp = second.next;
            second.next = prev;
            prev = second;
            second = tmp;
        
        # 3) Merge two halves 
        first, second = head, prev;
        # 2nd halve will be either equal or shorter, so we iterate over it
        while second:
            # Swap connections
            tmp1, tmp2 = first.next, second.next;
            first.next = second;
            second.next = tmp1;
            # Shifting pointers
            first, second = tmp1, tmp2;






        