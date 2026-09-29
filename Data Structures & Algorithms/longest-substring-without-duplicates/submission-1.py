class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        resLen = 0;

        for l in range(len(s)):
            r = l + 1;
            res = s[l];
            resLen = max(resLen, len(res));
            while r < len(s) and s[r] not in res:
                res += s[r];
                resLen = max(resLen, len(res));
                r += 1;

            # for r in range(l + 1, len(s)):
            #     if s[r] not in res:
            #         res += s[r];
            #         resLen = max(resLen, len(res));
            #     else:
            #         resLen = max(resLen, len(res));
            #         break;

        return resLen;