class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = dict()

        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                if hashMap[num] >= len(nums) / 2:
                    return num
                else:
                    hashMap[num] += 1
        
        return max(hashMap, key=hashMap.get)