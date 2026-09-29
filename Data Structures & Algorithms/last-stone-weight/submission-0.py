import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1. Convert to Max Heap (using negative numbers)
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap) # O(N) to build

        # 2. Simulation Loop
        while len(max_heap) > 1:
            # Get the two heaviest
            stone_1 = -heapq.heappop(max_heap) # Biggest
            stone_2 = -heapq.heappop(max_heap) # Second Biggest

            # Smash logic
            if stone_1 != stone_2:
                new_stone = stone_1 - stone_2
                heapq.heappush(max_heap, -new_stone)

        # 3. Edge Case: If no stones left, return 0
        if len(max_heap) == 0:
            return 0
            
        return -max_heap[0]