class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # Left is empty if we're at the start OR the previous element is 0
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                # Right is empty if we're at the end OR the next element is 0
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1

            if n <= 0:
                return True

        return n <= 0
            
