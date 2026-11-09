class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Step 1: Start by assuming the entire first word is our prefix
        prefix = strs[0]
        
        # Step 2: Loop through the remaining words in the list
        for i in range(1, len(strs)):
            j = 0
            # Step 3: Compare characters of `prefix` and `strs[i]`
            # What condition should keep our while-loop running?
            while j < len(prefix) and j < len(strs[i]):
                # If characters don't match, what should we do?
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            
            # Step 4: After comparing, shrink `prefix` to only the matching part
            prefix = prefix[:j]
            
        return prefix

