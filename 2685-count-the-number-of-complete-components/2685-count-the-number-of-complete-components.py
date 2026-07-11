class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        # Build adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            stack = [node]
            nodes = 0
            edge_count = 0

            while stack:
                curr = stack.pop()
                if visited[curr]:
                    continue

                visited[curr] = True
                nodes += 1
                edge_count += len(graph[curr])

                for nei in graph[curr]:
                    if not visited[nei]:
                        stack.append(nei)

            # Each edge is counted twice
            return nodes, edge_count // 2

        ans = 0

        for i in range(n):
            if not visited[i]:
                nodes, edge_count = dfs(i)

                # Check if component is complete
                if edge_count == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans