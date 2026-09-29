class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # resLen = 0;

        # for l in range(len(s)):
        #     r = l + 1;
        #     res = s[l];
        #     resLen = max(resLen, len(res));
        #     while r < len(s) and s[r] not in res:
        #         res += s[r];
        #         resLen = max(resLen, len(res));
        #         r += 1;
        # return resLen;
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            
            res = max(res, r - l + 1)
            
        return res