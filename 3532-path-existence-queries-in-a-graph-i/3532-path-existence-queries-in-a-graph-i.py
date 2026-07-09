class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        comp = [0] * n
        comp_id = 0 
        for i in range(1,n):
            if nums[i] - nums[i-1] <= maxDiff:
                comp[i] = comp_id
            else:
                comp_id +=1 
                comp[i] = comp_id

        ans= []
        for u, v in queries:
            ans.append(comp[u] == comp[v])
        return ans
