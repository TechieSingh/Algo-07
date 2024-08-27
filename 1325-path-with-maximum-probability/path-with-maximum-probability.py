class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        result=0
        weigth=0

        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src,dst=edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src,succProb[i]])
        pq=[(-1, start_node)] 
        visited=set()

        while pq:
            prop, cur = heapq.heappop(pq)
            visited.add(cur)

            if cur==end_node:
                return prop *-1
            for nei, edgeprop in adj[cur]:
                if nei not in visited:
                    heapq.heappush(pq,(prop*edgeprop,nei))
            

        return result
        