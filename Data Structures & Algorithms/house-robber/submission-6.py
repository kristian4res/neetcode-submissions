class Solution:
    def rob(self, nums: List[int]) -> int:
        two_houses_ago_max = 0
        previous_house_max = 0

        for current_house_value in nums:
            # The Core Decision
            rob_current = current_house_value + two_houses_ago_max
            skip_current = previous_house_max
            
            current_max = max(rob_current, skip_current)

            # Slide the window forward
            two_houses_ago_max = previous_house_max
            previous_house_max = current_max
            
        return previous_house_max