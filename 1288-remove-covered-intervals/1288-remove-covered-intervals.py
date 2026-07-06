class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: sort by left asc, right desc
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        max_right = 0
        
        # Step 2: scan
        for l, r in intervals:
            if r <= max_right:
                # covered → skip
                continue
            else:
                # not covered → count it
                count += 1
                max_right = r
        return count