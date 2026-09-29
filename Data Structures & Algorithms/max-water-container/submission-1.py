class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Find largest product -> maximise length and minimise height diff 
        maxProd = 0;
        curProd = 0;

        # Use two pointer
        l, r = 0, len(heights) - 1;

        while (l < r):
            length = r - l;
            minHeight = min(heights[l], heights[r]);
            curProd = minHeight * length;
            if (curProd > maxProd):
                maxProd = curProd;
            
            if (heights[l] > heights[r]):
                r -= 1;
            else:
                l += 1;

        return maxProd
        