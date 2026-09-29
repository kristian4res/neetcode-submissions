class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # set vars
        numIntervals = 0;

        # sort in ascending order
        sortedIntervals = sorted(intervals);

        # edge case guard clause
        if len(intervals) == 1:
            return 0;
        

        # iterate over array
        curEnd = sortedIntervals[0][1];

        for i in range(1, len(sortedIntervals)):
            if sortedIntervals[i][0] < curEnd:
                numIntervals += 1;
                curEnd = min(curEnd, sortedIntervals[i][1])
            else:
                curEnd = sortedIntervals[i][1];
        
        return numIntervals;
