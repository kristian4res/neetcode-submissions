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
        curIndex = 0;

        while (curNode.next != None):
            print(curNode.val)
            if (seen.get(curNode.val)):
                return True;

            seen[curNode.val] = curIndex;
            curIndex += 1;
            curNode = curNode.next;
        
        curIndex = -1;
        return False;