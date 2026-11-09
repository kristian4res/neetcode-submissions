class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1          # Last valid element in nums1
        j = n - 1          # Last element in nums2
        last = m + n - 1   # Last position in nums1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[i], nums1[last] = nums1[last], nums1[i]
                i -= 1
                pass
            else:
                nums2[j], nums1[last] = nums1[last], nums2[j]
                j -= 1
                pass
            
            last -= 1