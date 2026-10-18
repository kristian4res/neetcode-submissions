class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        # Build counts for s1 and the first window in s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        # Number of characters whose counts currently match
        matches = 0
        for i in range(26):
            if s1_count[i] == window_count[i]:
                matches += 1

        left = 0

        # Expand and shrink the sliding window
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Add s2[right]
            index = ord(s2[right]) - ord('a')
            window_count[index] += 1

            if window_count[index] == s1_count[index]:
                matches += 1
            elif window_count[index] == s1_count[index] + 1:
                matches -= 1

            # Remove s2[left]
            index = ord(s2[left]) - ord('a')
            window_count[index] -= 1

            if window_count[index] == s1_count[index]:
                matches += 1
            elif window_count[index] == s1_count[index] - 1:
                matches -= 1

            left += 1

        # Check the final window
        return matches == 26