from typing import List

class MinHeap:
    def __init__(self):
        self.arr = [0]

    def push(self, val: int) -> None:
        self.arr.append(val)
        self._percolate_up(len(self.arr) - 1)

    def pop(self) -> int:
        if len(self.arr) == 1:
            print("empty heap")
            return -1
        
        if len(self.arr) == 2:
            return self.arr.pop()
        
        root_val = self.arr[1]
        # Move last element to root
        self.arr[1] = self.arr.pop()
        # Fix the order
        self._percolate_down(1)
        
        return root_val

    def top(self) -> int:
        if len(self.arr) == 1:
            print("empty heap")
            return -1
        return self.arr[1]

    def heapify(self, nums: List[int]) -> None:
        self.arr = [0] + nums[:]
        # Start from the last non-leaf node and go backwards to the root
        for i in range(len(self.arr) // 2, 0, -1):
            self._percolate_down(i)

    # --- Helpers ---

    def _percolate_up(self, i: int) -> None:
        while i > 1 and self.arr[i] < self.arr[i // 2]:
            self.arr[i], self.arr[i // 2] = self.arr[i // 2], self.arr[i]
            i = i // 2

    def _percolate_down(self, i: int) -> None:
        while 2 * i < len(self.arr):
            left = 2 * i
            right = 2 * i + 1
            smallest = left

            if right < len(self.arr) and self.arr[right] < self.arr[left]:
                smallest = right
            
            if self.arr[i] > self.arr[smallest]:
                self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
                i = smallest
            else:
                break