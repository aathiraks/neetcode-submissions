class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        if len(edges) > n - 1:
            return False
        
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(curr, prev):
            # check if already visited
            if curr in visit:
                return False
            
            # add to visited
            visit.add(curr)

            for new in adj[curr]:
                if new == prev:
                    continue
                
                if not dfs(new, curr):
                    return False
            
        return True

        return dfs(0, -1) and len(visit) == n