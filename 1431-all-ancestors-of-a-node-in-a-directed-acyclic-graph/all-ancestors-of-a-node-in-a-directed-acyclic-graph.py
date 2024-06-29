class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize the result list and direct child adjacency list
        ans = [[] for _ in range(n)]
        directChild = defaultdict(list)
        
        # Build the adjacency list
        for parent, child in edges:
            directChild[parent].append(child)
        
        # Perform DFS for each node
        for i in range(n):
            self.dfs(i, i, ans, directChild)
        
        # Sort the ancestors list for each node
        for lst in ans:
            lst.sort()
        
        return ans

    def dfs(self, ancestor: int, curr: int, ans: List[List[int]], directChild: defaultdict) -> None:
        # Traverse all children of the current node
        for child in directChild[curr]:
            if ancestor not in ans[child]:
                ans[child].append(ancestor)
                self.dfs(ancestor, child, ans, directChild)
