class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        return [1] + digits
        # If we exit the loop, every digit was a 9 (e.g., [9, 9] -> [0, 0])
        # What should we return here?
