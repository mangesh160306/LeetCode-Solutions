class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((nums[i], i) for i in range(n))

        values = [0] * n
        pos = [0] * n
        for i, (v, idx) in enumerate(arr):
            values[i] = v
            pos[idx] = i

        # Connected components
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        # nxt[i] = furthest sorted index reachable in one edge
        nxt = [0] * n
        r = 0
        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            nxt[l] = r

        LOG = (n).bit_length()
        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        ans = []

        for u, v in queries:
            u = pos[u]
            v = pos[v]

            if u == v:
                ans.append(0)
                continue

            if u > v:
                u, v = v, u

            if comp[u] != comp[v]:
                ans.append(-1)
                continue

            cur = u
            steps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < v:
                    steps += 1 << k
                    cur = up[k][cur]

            ans.append(steps + 1)

        return ans
        