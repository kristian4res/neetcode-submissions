class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const frequencyMap = new Map();
        for (const num of nums) {
            frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
        }

        const sortedFrequencies = Array.from(frequencyMap.entries()).sort(([, freqA], [, freqB]) => freqB - freqA);

        const result = [];
        for (let i = 0; i < k; i++) {
            result.push(parseInt(sortedFrequencies[i][0])); // Parse back to integer
        }

        return result;
    }
}
