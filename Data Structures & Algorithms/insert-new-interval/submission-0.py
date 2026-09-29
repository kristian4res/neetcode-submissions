class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # start, end = 0, 1;
        # res = [];

        # for i in range(len(intervals)):
        #     newStart, newEnd = newInterval[start], newInterval[end];
        #     if newStart < intervals[i][start] and newEnd < intervals[i][start]:
        #         print('insert here');
        #         res.append(newInterval);

        #     if (newStart >= intervals[i][start] and newStart <= intervals[i][end]) or (newEnd >= intervals[i][start] and newEnd <= intervals[i][end]):
        #         print('overlap detected');
        #         newInterval = [min(newStart, intervals[i][start]), max(newEnd, intervals[i][end])];

        #     print('shift left');
        #     res.append([intervals[i][start], intervals[i][end]])

    
        
        # return res;
        res = []
        
        for i, current_interval in enumerate(intervals):
            # Case 1: Current is strictly to the Right of New (We found the spot!)
            if current_interval[0] > newInterval[1]:
                res.append(newInterval);
                return res + intervals[i:];
            
            # Case 2: Current is strictly to the Left of New
            elif current_interval[1] < newInterval[0]:
                res.append([current_interval[0], current_interval[1]]);
                
            # Case 3: Overlap
            else:
                newInterval = [min(newInterval[0], current_interval[0]), max(newInterval[1], current_interval[1])]
        
        res.append(newInterval)
        return res