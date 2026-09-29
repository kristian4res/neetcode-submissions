class Solution:
    def binarySearch(self, arr: List[int], target: int):
        l, r = 0, len(arr) - 1;

        while (l <= r):
            m = (l + r) // 2

            if (target > arr[m]):
                l = m + 1
            elif (target < arr[m]):
                r = m - 1
            else:
                return m
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx = 0
        while idx <= len(matrix) - 1:
            if ((target >= matrix[idx][0]) and (target <= matrix[idx][len(matrix[idx])-1])):
                res = self.binarySearch(matrix[idx], target)
                if res != -1:
                    return True
            idx += 1
        return False