class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Empty tree
        if not n:
            return True

        # Cyclic
        if len(edges) > n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(curr, prev):
            # already visited
            if curr in visit:
                return False
            
            # newly visited
            visit.add(curr)

            # traverse through the neighbours
            for neighbor in adj[curr]:
                if neighbor == prev:
                    continue
                
                if not dfs(neighbor, curr):
                    return False
            
            return True

        return dfs(0, -1) and len(visit) == n