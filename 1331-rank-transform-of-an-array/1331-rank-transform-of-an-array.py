class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
         # Step 1: Sort unique elements
        sorted_unique = sorted(set(arr))
        
        # Step 2: Map values to ranks
        rank_map = {val: i+1 for i, val in enumerate(sorted_unique)}
        
        # Step 3: Transform array
        return [rank_map[val] for val in arr]