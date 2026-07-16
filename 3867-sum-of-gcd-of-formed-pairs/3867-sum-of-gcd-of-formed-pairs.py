class Solution:
    def gcdSum(self, nums: list[int]) -> int:

        prefixGcd = []
        mx = 0
        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(math.gcd(num, mx))

        prefixGcd.sort()

        total = 0
        i, j = 0, len (prefixGcd) - 1
        while i < j :
            total += math.gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return total         