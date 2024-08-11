import collections
from typing import List

class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # You can choose any of the below methods to find the network delay time.
        # Here, I'll use Dijkstra as it's most efficient for this problem.

        return self.Dijkstra(times, n, k)
    
    def BellmanFord(self, times, N, K):
        # Bellman-Ford Algorithm
        cost = {i: float('inf') for i in range(1, N + 1)}
        cost[K] = 0
        for _ in range(N - 1):
            update = False
            for u, v, c in times:
                if cost[u] + c < cost[v]:
                    update = True
                    cost[v] = cost[u] + c
            if not update:
                break
        
        ans = max(cost.values())
        return ans if ans != float('inf') else -1
    
    def Dijkstra(self, times, N, K):
        g = collections.defaultdict(list)
        for u, v, c in times:
            g[u].append((v, c))
        
        cost = {i: float('inf') for i in range(1, N + 1)}
        cost[K] = 0
        from queue import PriorityQueue
        pq = PriorityQueue()
        pq.put((0, K))
        
        while not pq.empty():
            curr_cost, curr_node = pq.get()
            
            for nei, c in g[curr_node]:
                if curr_cost + c < cost[nei]:
                    cost[nei] = curr_cost + c
                    pq.put((cost[nei], nei))
        
        ans = max(cost.values())
        return ans if ans != float('inf') else -1
    
    def DFS(self, times, N, K):
        cost = {i: float('inf') for i in range(1, N + 1)}
        g = collections.defaultdict(list)
        for u, v, c in times:
            g[u].append((v, c))
        
        def dfs(curr, curr_cost):
            if curr_cost < cost[curr]:
                cost[curr] = curr_cost
                for nei, c in g[curr]:
                    dfs(nei, curr_cost + c)
        
        dfs(K, 0)
        ans = max(cost.values())
        return ans if ans != float('inf') else -1
    
    def BFS(self, times, N, K):
        g = collections.defaultdict(list)
        for u, v, c in times:
            g[u].append((v, c))
        
        cost = {i: float('inf') for i in range(1, N + 1)}
        cost[K] = 0
        curr = collections.deque()
        curr.append((K, 0))
        
        while curr:
            curr_node, curr_cost = curr.popleft()
            for nei, c in g[curr_node]:
                if curr_cost + c < cost[nei]:
                    cost[nei] = curr_cost + c
                    curr.append((nei, curr_cost + c))
        
        ans = max(cost.values())
        return ans if ans != float('inf') else -1

    def FloydWarshall(self, times, N, K):
        # Floyd-Warshall Algorithm
        cost = {}
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:
                    cost[(i, j)] = 0
                else:
                    cost[(i, j)] = float('inf')
        
        for u, v, c in times:
            cost[(u, v)] = c
            
        for k in range(1, N + 1):
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    cost[(i, j)] = min(cost[(i, j)], cost[(i, k)] + cost[(k, j)])
        
        ans = float('-inf')
        for i in range(1, N + 1):
            ans = max(ans, cost[(K, i)])
        
        return ans if ans != float('inf') else -1
