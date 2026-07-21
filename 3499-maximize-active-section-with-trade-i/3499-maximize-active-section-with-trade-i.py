class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        original = s.count('1')

        # Run-length encoding: (character, length)
        runs = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        ans = original

        # Check every internal block of 1's
        for i in range(2, len(runs) - 2, 2):
            left_zero = runs[i - 1][1]
            right_zero = runs[i + 1][1]
            ans = max(ans, original + left_zero + right_zero)

        return ans