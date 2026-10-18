class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        longest = 0
        
        for right in range(len(s)):
            # 1. Expand the window by adding the current character to counts
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # Track the highest frequency of any single character in the window
            max_freq = max(max_freq, count[s[right]])
            
            # 2. Window length is (right - left + 1).
            # If the number of replacements needed > k, shrink from the left.
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            # 3. Update the maximum valid window size
            longest = max(longest, right - left + 1)
            
        return longest


        