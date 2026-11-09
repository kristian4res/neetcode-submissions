class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        return cur.val if cur and index == 0 else -1

    def insertHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head.next
        if not new.next:
            self.tail = new

        self.head.next = new
        return  

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        return


    def remove(self, index: int) -> bool:
        cur = self.head
        while cur and index > 0:
            cur = cur.next
            index -= 1
        
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        res = []
        cur = self.head.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
