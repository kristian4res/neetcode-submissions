# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import defaultdict;

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = defaultdict();
        curNode = head;

        while (curNode):
            if (seen.get(curNode.val) == curNode):
                return True;

            seen[curNode.val] = curNode;
            curNode = curNode.next;

        return False;