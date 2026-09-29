# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def sort(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next


    def divide(self, lists: List[Optional[ListNode]], s: int, e: int):
        if s > e:
            return None
        if s == e:
            return lists[s]

        mid = s + (e - s) // 2

        left = self.divide(lists, s, mid)
        right = self.divide(lists, mid + 1, e)

        return self.sort(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists) - 1)